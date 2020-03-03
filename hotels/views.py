from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Room, Hotel


class IndexView(generic.ListView):
    template_name = 'hotels/index.html'
    context_object_name = 'latest_hotel_list'

    def get_queryset(self):
        """
        Return the last five published hotel (not including those set to be
        published in the future).
        """
        return Hotel.objects.filter(
        act_date__lte=timezone.now()
        ).order_by('-act_date')[:5]


class DetailView(generic.DetailView):
    model = Hotel
    template_name = 'hotels/detail.html'
    
    def get_queryset(self):
        """
        Excludes any hotels that aren't published yet.
        """
        return Hotel.objects.filter(act_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Hotel
    template_name = 'hotels/results.html'

def rating(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    try:
        selected_room = hotel.room_set.get(pk=request.POST['room'])
    except (KeyError, Room.DoesNotExist):
        # Redisplay the hotel rating form.
        return render(request, 'hotels/detail.html', {
            'hotel': hotel,
            'error_message': "You didn't select a room.",
        })
    else:
        selected_room.rating += 1
        selected_room.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('hotels:results', args=(hotel.id,)))

def results(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotels/results.html', {'hotel': hotel}) 