from django.contrib import admin
from .models import Deck, Card

def push_live(modeladmin, request, querryset):
    rows_updated = querryset.update(is_active=True)
    if rows_updated == 1:
        message_bit = "1 dock was"
    else:
        message_bit = "%s decks were" % rows_updated
        modeladmin  .message_user(request, "%s successfully marked as active." % message_bit) 

push_live.short_description = "Mark Selected Decks as active"

class DeckAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'get_number_of_cards')
    list_filter = ('is_active',)
    search_fields = ['title', 'description']
    actions = [push_live]


class CardAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Deck, DeckAdmin)

admin.site.register(Card, CardAdmin)