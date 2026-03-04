from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, Kategori, Status
from .forms import ProdukForm
import requests
import hashlib
from datetime import datetime

#importtt user dan password otomatis
def import_api(request):
    #API
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    
    now = datetime.now()
    
    #password MD5
    tanggal = now.strftime("%d")
    bulan = now.strftime("%m")
    tahun = now.strftime("%y")
    
    string_password = f"bisacoding-{tanggal}-{bulan}-{tahun}"
    #ubah ke MD5
    password_hash = hashlib.md5(string_password.encode()).hexdigest()

    #username (tesprogrammer260126C21)
    username_dynamic = f"tesprogrammer{tanggal}{bulan}{tahun}C{now.strftime('%H')}"

    #form data
    payload = {
        'username': username_dynamic,
        'password': password_hash
    }

    print(f"Mencoba login dengan User: {username_dynamic} | Pass: {string_password}")

    try:
        #request POST
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            data_json = response.json()
            
            #cek session
            if 'error' in data_json and data_json['error']:
                print(f"API Error: {data_json['ket']}")
                return render(request, 'index.html', {'error_msg': data_json['ket']})

            items = data_json.get('data', [])
            
            for item in items:
                #field kategori
                kat_obj, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
                #field status
                stat_obj, _ = Status.objects.get_or_create(nama_status=item['status'])
                
                try:
                    harga_clean = int(item['harga'])
                except:
                    harga_clean = 0

                #field produk
                Produk.objects.get_or_create(
                    nama_produk=item['nama_produk'],
                    defaults={
                        'harga': harga_clean,
                        'kategori': kat_obj,
                        'status': stat_obj
                    }
                )
    except Exception as e:
        print(f"Error Script: {e}")

    return redirect('index')

def index(request):
    #filter hanya yang "bisa dijual"
    produk_list = Produk.objects.filter(status__nama_status__iexact='bisa dijual')
    return render(request, 'index.html', {'produk_list': produk_list})

def tambah(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdukForm()
    return render(request, 'form.html', {'form': form, 'judul': 'Tambah Produk'})

def edit(request, id):
    produk_obj = get_object_or_404(Produk, id=id)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk_obj)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProdukForm(instance=produk_obj)
    return render(request, 'form.html', {'form': form, 'judul': 'Edit Produk'})

def hapus(request, id):
    produk_obj = get_object_or_404(Produk, id=id)
    produk_obj.delete()
    return redirect('index')