from django.contrib import admin
from .models import Post
from .models import SimulatedTrade, VirtualBalance, SimulationSession



admin.site.register(SimulatedTrade)
admin.site.register(VirtualBalance)
admin.site.register(SimulationSession)
admin.site.register(Post)