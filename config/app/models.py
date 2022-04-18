from django.db import models


class Season(models.Model):
    CHOICES = (
        ("SUMMER", "SUMMER"),
        ("WINTER", "WINTER"),
        ("SPRING", "SPRING"),
        ("FALL", "FALL"),
    )
    title = models.CharField(
        max_length=8,
        null=False,
        unique=True,
        db_index=True,
        choices=CHOICES,
        verbose_name="Title",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Season"
        verbose_name_plural = "Seasons"
        default_related_name = "seasons"


class Type(models.Model):
    title = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        db_index=True,
        verbose_name="Type",
    )

    def save(self, *args, **kwargs) -> None:
        self.title = self.title.upper()
        super(Type, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Item(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Title",
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name="Type",
    )
    season = models.ManyToManyField(
        "Season",
        related_name="item_season",
        verbose_name="Season",
    )
    image = models.URLField(
        max_length=250,
        null=False,
        verbose_name="Image Link",
    )

    def save(self, *args, **kwargs) -> None:
        self.title = self.title.upper()
        super(Item, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
