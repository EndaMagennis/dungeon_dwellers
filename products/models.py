from datetime import datetime, timedelta
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


# Create your models here.
class Category(models.Model):
    """A model for product categories."""
    # The Category model has two fields: name and friendly_name.
    name = models.CharField(
        max_length=255,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Category Name'
        )
    friendly_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        # The Meta class is used to define metadata for the model.
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        # The __str__ method returns the name of the category.
        return self.name
    
    def get_friendly_name(self):
        # The get_friendly_name method returns the friendly name of the category.
        return self.friendly_name

class Tag(models.Model):
    """A model for product tags."""
    # The Tag model has two fields: name and friendly_name.
    name = models.CharField(
        max_length=255,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Tag Name'
    )
    friendly_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At',
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At',
        null=True
    )

    class Meta:
        # The Meta class is used to define metadata for the model.
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        # The __str__ method returns the name of the tag.
        return self.name
    
    def get_friendly_name(self):
        # The get_friendly_name method returns the friendly name of the tag.
        return self.friendly_name
    

class Product(models.Model):
    """A model for products."""
    # The Product model has six fields: category, sku, name, description, price and image_url.
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='products',
        verbose_name='Tags'
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Product Slug',
    )
    sku = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Product Name'
    )
    description = models.TextField(
        max_length=1024,
        null=False,
        blank=False,
        verbose_name='Product Description'
    )
    has_dimensions = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )
    has_quantity = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )
    is_promoted = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )
    dimensions = models.IntegerField(
        null=True,
        blank=True,
        help_text='Product dimensions is height in cm'
    )
    quantity = models.IntegerField(
        null=True,
        blank=True
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        # The Meta class is used to define metadata for the model.
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def __str__(self):
        # The __str__ method returns the name of the product.
        return self.name
    
    def generate_sku(self):
        # The generate_sku method generates a SKU for the product.
        return f'{self.name}-{datetime.now().strftime("%Y%m%d%H%M%S%f")}'
    
    def save(self, *args, **kwargs):
        # The save method saves the product to the database.
        if not self.sku:
            self.sku = self.generate_sku()
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_tags(self):
        # The get_tags method returns the tags of the product.
        return self.tags.all()
    
    def get_main_image(self):
        # The get_main_image method returns the main image of the product.
        images = ProductImage.objects.filter(product=self)
        if images.exists():
            active_images = images.filter(is_active=True)
            if active_images.exists():
                default_image = active_images.filter(default_image=True)
                if default_image.exists():
                    return default_image.first().image_url
                else:
                    return active_images.first().image_url


class ProductImage(models.Model):
    """A model for product images."""
    # The ProductImage model has two fields: product and image.
    product = models.ForeignKey(
        'Product',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='images'
    )
    image = CloudinaryField(
        'product_image',
        folder='product_images',
        null=False,
        blank=False
    )
    alt_text = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Alt Text'
    )
    default_image = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Updated At'
    )

    class Meta:
        # The Meta class is used to define metadata for the model.
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
        ordering = ['product']

    def __str__(self):
        # The __str__ method returns the name of the product image.
        return self.product.name
    
    def save(self, *args, **kwargs):
        # The save method saves the product image to the database.
        if self.default_image:
            for image in ProductImage.objects.filter(product=self.product):
                if image != self:
                    image.default_image = False
                    image.save()
        
    @property
    def image_url(self):
        # The image_url property returns the URL of the image.
        if self.image:
            return self.image.url
        return 'static/images/placeholder.jpg'
    