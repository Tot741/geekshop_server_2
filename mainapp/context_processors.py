from basket.models import Basket


def basket_count(request):
    print(f'context processor basket works')

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)
        return {'basketcount': sum(basket.quantity for basket in baskets)}
    else:
        return {'basketcount': 0}
