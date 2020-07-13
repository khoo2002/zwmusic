from django.shortcuts import render
from django.http import HttpResponse
from convert import forms
import youtube_dl
import os
import requests
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')    
    import shutil
    if os.path.isfile('download')==True:
        shutil.rmtree('download')
        os.mkdir('download')
    return render(
        request,
        'index.html',
        {
            'rlt': request.POST.get('form-url','None'),
            'title':'ZWQQ_MUSIC_CONVERTER',
            'form': forms.ZWForm, 
            'message':'this is a form',
         }
        )


def converter(request):
    # return HttpResponse('Hello from Python!')
    return render(
        request,
        'converter.html',
        {
            'title':'ZWQQ_MUSIC_CONVERTER',
            'form': forms.ZWForm, 
            'message':'this is a form',
            
         }
        )
        
 
def readydl(request):
    t_url = ['']
    furl=[]
    fid=[]
    url = request.POST['t_url']
    ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best',
                                'extractaudio': True,
                                'audioformat': "mp4",
                                'outtmpl': 'download/%(id)s' + '.mp4',
                                'noplaylist': True,}) 
    # Add all the available extractors 
    ydl.add_default_info_extractors() 
    result = ydl.extract_info(url, download=True) 
    id = result['id']
    title = result['title']
    symbol = []
    import re
    if re.findall(r'[,|.|《|》|||“|”|。|，|?|？|-|—|_|+|&|&|￥|$|!|！|~|·|`|~|】|【|「|」]',title):
        title=re.sub(r'[,|.|《|》|||“|”|。|，|?|？|-|—|_|+|&|&|￥|$|!|！|~|·|`|~|】|【|「|」]',r'',title)
    import subprocess
    cmd = ['ffmpeg','-i', 'download/'+id+'.mp4','-vn','-f','mp3', 'download/'+id+'.mp3']
    out = subprocess.run(cmd)
    surl= 'readydl/'+id +'.mp3/'+title+'.mp3'
    furl.append(surl)
    fid.append(title)
    filename = title+'.mp3'
    return render(request,'converter.html',{'dlurl':furl[0],'context':fid[0]+'.mp3'}) 


    

def download(request,dlfile,file):
    f =open('download/'+dlfile,'rb')
    response = HttpResponse(f.read(),'utf-8')
    response['Content-Deposition'] = 'attachment; filename="'+ dlfile +'.mp3"'
    response['content_type'] = 'audio/mp3'
    return response


def indexdownload(request,dlfile,file):
    f =open('index/'+dlfile,'rb')
    response = HttpResponse(f.read(),'utf-8')
    response['Content-Deposition'] = 'attachment; filename="'+ dlfile +'.mp3"'
    response['content_type'] = 'audio/mp3'
    return response

def mp4tomp3():
    video=request.FILES['video']
    import subprocess
    cmd = ['ffmpeg','-i', 'download/'+id+'.mp4','-vn','-f','mp3', 'download/'+id+'.mp3']
    out = subprocess.run(cmd)
    surl= 'readydl/'+id +'.mp3/'+title+'.mp3'
    furl.append(surl)
    fid.append(title)
    filename = title+'.mp3'
    return render(request,'converter.html',{'dlurl':furl[0],'context':fid[0]+'.mp3'}) 

def picture(imgnfile):
    f = open(imgnfile,'rb')
    response = HttpResponse(f.read(),'utf-8')
    response['Content-Deposition'] = 'attachment; filename="'+ imgnfile +'.jpg"'
    response['content_type'] = 'image/jpg'
    return response

def qrcode(request):
    return render(
        request,
        'qrcode.html',
        {
            'title':'ZWQQ_MUSIC_CONVERTER',
            'form': forms.ZWForm, 
            'message':'this is a form',
            
         }
        )

def dlqrcode(request):
    content = request.POST['t_url']
    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('zwqrcode.png')
    filename = 'zwqrcode.png'
    dl_filename = 'zwqrcode.png'
    f = open(dl_filename,'rb')
    response = HttpResponse(f.read())
    response['Content-Deposition'] = 'attachment; filename="zwqrcode.png"'
    response['content_type'] = 'image/png'
    return response

#function for calling the ffmpeg buildpack
#def test(request):
#    import subprocess
#    cmd = ['ffmpeg','-i','index/qq.mp4','-vn','-f','mp3', 'index/qq.mp3']
#    out = subprocess.run(cmd)
#    qq=['index/qq.mp3']
#    return render(request,'test.html',{'msg':qq[0]})
    
    
#function for download 
#def btntest(request,file):
#    f =open('index/'+file+'.mp3','rb')
#    response = HttpResponse(f.read(),'utf-8')
#    response['Content-Deposition'] = 'attachment; filename="index/'+file+'.mp3"'
#    response['content_type'] = 'audio/mp3'
#    return response
