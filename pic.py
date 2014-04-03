import os,sys
import Image


im = Image.open('test.png')
rgb_im = im.convert('RGB')
bin=''

w,h =  im.size
im_out= Image.new('RGB', (w,h))
pix=im_out.load()

for i in range(0,w):
    for j in range(0,h):
        r, g, b = rgb_im.getpixel((j, i))
        r=r & 1
        g=g & 1
        b=b & 1
        rr=r<<8
        gg=g<<8
        bb=b<<8
        
        pix[j,i]=(rr,gg,bb)

                        
for i in range(0,120):
#    if (i%2 != 0):
#        continue
    r, g, b = rgb_im.getpixel((i, 0))
                        
    bin+=str(r & 0x1)
    bin+=str(g & 0x1)
    bin+=str(b & 0x1)

    rr=r<<8
    gg=g<<8
    bb=b<<8


    print i,':',r,g,b



print bin
im_out.save('out.png')    
im_out.show();

