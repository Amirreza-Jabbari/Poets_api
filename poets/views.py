import random
import re

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import GolestanHikayat, Hafez, Khayyam, Moulavi
from .serializers import (
    GolestanHikayatSerializer,
    HafezSerializer,
    KhayyamSerializer,
    MoulaviSerializer,
)

class GolestanHikayatView(APIView):
    # map integer → Persian bab
    BAB_MAP = {
        1: 'باب اول',  2: 'باب دوم', 3: 'باب سوم', 4: 'باب چهارم',
        5: 'باب پنجم', 6: 'باب ششم', 7: 'باب هفتم', 8: 'باب هشتم',
    }

    def get(self, request, bab=None, hekayat=None):
        qs = GolestanHikayat.objects.all()
        if bab:
            bab_str = self.BAB_MAP.get(bab)
            if not bab_str:
                return Response({'detail': 'Invalid bab'}, status=400)
            qs = qs.filter(bab=bab_str)
            if hekayat:
                try:
                    obj = qs.get(hekayat=hekayat)
                except GolestanHikayat.DoesNotExist:
                    return Response({'detail': 'Not found'}, status=404)
                return Response(GolestanHikayatSerializer(obj).data)
            # random in this bab
            obj = random.choice(list(qs))
            return Response(GolestanHikayatSerializer(obj).data)

        # no bab → random from all
        obj = random.choice(list(qs))
        return Response(GolestanHikayatSerializer(obj).data)


class HafezView(APIView):
    CATS = ('ghazal', 'ghete', 'robaee', 'ghaside', 'montasab')

    def get(self, request, cat=None, num=None):
        qs = Hafez.objects.all()
        if cat:
            if cat not in self.CATS:
                return Response({'detail': 'Invalid category'}, status=400)
            qs = qs.filter(urn__contains=f'hafez.{cat}')
            if num:
                urn_str = f'urn:cts:perslit:hafez.{cat}:{num}'
                try:
                    obj = qs.get(urn=urn_str)
                except Hafez.DoesNotExist:
                    return Response({'detail': 'Not found'}, status=404)
                return Response(HafezSerializer(obj).data)
            # random in cat
            obj = random.choice(list(qs))
            return Response(HafezSerializer(obj).data)
        # no cat → random overall
        obj = random.choice(list(qs))
        return Response(HafezSerializer(obj).data)


class KhayyamView(APIView):
    CATS = ('robaee', 'tarane')

    def get(self, request, cat=None, num=None):
        qs = Khayyam.objects.all()
        if cat:
            if cat not in self.CATS:
                return Response({'detail': 'Invalid category'}, status=400)
            qs = qs.filter(urn__contains=f'khayyam.{cat}')
            if num:
                if cat == 'tarane':
                    # tarane by section field
                    target = f'ترانه شمارهٔ {num}'
                    try:
                        obj = qs.get(section__icontains=target)
                    except Khayyam.DoesNotExist:
                        return Response({'detail': 'Not found'}, status=404)
                else:
                    # robaee by URN
                    urn_str = f'urn:cts:perslit:khayyam.{cat}:{num}'
                    try:
                        obj = qs.get(urn=urn_str)
                    except Khayyam.DoesNotExist:
                        return Response({'detail': 'Not found'}, status=404)
                return Response(KhayyamSerializer(obj).data)

            # random in cat
            obj = random.choice(list(qs))
            return Response(KhayyamSerializer(obj).data)

        # no cat → random overall
        obj = random.choice(list(qs))
        return Response(KhayyamSerializer(obj).data)

class MoulaviView(APIView):
    # Supported categories and their urn patterns
    CATS = (
        'shams:ghazalsh',
        'shams:mostadrakat',
        'shams:tarjeeat',
        'shams:robaeesh',
        'masnavi:daftar1',
        'masnavi:daftar2',
        'masnavi:daftar3',
        'masnavi:daftar4',
        'masnavi:daftar5',
        'masnavi:daftar6',
    )

    def get(self, request, cat=None, num=None):
        qs = Moulavi.objects.all()
        if cat:
            if cat not in self.CATS:
                return Response({'detail': 'Invalid category'}, status=400)
            qs = qs.filter(urn__contains=f'moulavi.{cat}')
            if num:
                # For shams categories, urn is like: urn:cts:perslit:moulavi.shams:ghazalsh.1
                # For masnavi categories, urn is like: urn:cts:perslit:moulavi.masnavi:daftar1.1
                if cat.startswith('shams:'):
                    urn_str = f'urn:cts:perslit:moulavi.{cat}.{num}'
                else:
                    # masnavi:daftarX
                    urn_str = f'urn:cts:perslit:moulavi.{cat}.{num}'
                try:
                    obj = qs.get(urn=urn_str)
                except Moulavi.DoesNotExist:
                    return Response({'detail': 'Not found'}, status=404)
                return Response(MoulaviSerializer(obj).data)
            # random in cat
            obj = random.choice(list(qs))
            return Response(MoulaviSerializer(obj).data)
        # no cat → random overall
        obj = random.choice(list(qs))
        return Response(MoulaviSerializer(obj).data)