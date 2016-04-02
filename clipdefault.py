# -*- coding:utf-8 -*-
from PIL import Image
import os, sys

#裁剪压缩图片
def clipResizeImg(im, dst_w, dst_h,disimgpath, qua=100):
	'''
		先按照一个比例对图片剪裁，然后在压缩到指定尺寸
		一个图片 16:5 ，压缩为 2:1 并且宽为200，就要先把图片裁剪成 10:5,然后在等比压缩
	'''
	ori_w,ori_h = im.size

	dst_scale = float(dst_w) / dst_h #目标高宽比
	ori_scale = float(ori_w) / ori_h #原高宽比

	if ori_scale <= dst_scale:
		#过高
		width = ori_w
		height = int(width/dst_scale)

		x = 0
		y = (ori_h - height) / 2

	else:
		#过宽
		height = ori_h
		width = int(height*dst_scale)

		x = (ori_w - width) / 2
		y = 0

	#裁剪
	box = (x,y,width+x,height+y)
	#这里的参数可以这么认为：从某图的(x,y)坐标开始截，截到(width+x,height+y)坐标
	#所包围的图像，crop方法与php中的imagecopy方法大为不一样
	newIm = im.crop(box)
	im = None

	#压缩
	ratio = float(dst_w) / width
	newWidth = int(width * ratio)
	newHeight = int(height * ratio)
	newIm.resize((newWidth,newHeight),Image.ANTIALIAS).save(disimgpath, "PNG",quality=100)
	print  "old size  %s  %s"%(ori_w, ori_h)
	print  "new size %s %s"%(newWidth, newHeight)
	print  "剪裁后等比压缩完成"

if __name__ == '__main__':
    
    #	$1 oriimgpath   $2 dstimgpath
    
    oriimgpath = sys.argv[1]
        
        dstimgpath = sys.argv[2]
        
        img = Image.open(oriimgpath)
        
        #	1242 * 2208   Default-414w-736h@3x.png   retina HD 5.5
        img = Image.open(oriimgpath)
        clipResizeImg(img,1242,2208,dstimgpath+'/Default-414w-736h@3x-s.png')
        img = Image.open(dstimgpath+'/Default-414w-736h@3x-s.png')
        if not (img.size == (1242,2208)):
            clipResizeImg(img,1242,2208,dstimgpath+'/Default-414w-736h@3x.png')
        else:
            print 'default clip completed,terminated'
        os.system('rm -r '+dstimgpath+'/Default-414w-736h@3x-s.png')
        
        #	750 * 1334    Default-375w-667h@2x.png   retina HD 4.7
        img = Image.open(oriimgpath)
        clipResizeImg(img,750,1334,dstimgpath+'/Default-375w-667h@2x-s.png')
        img = Image.open(dstimgpath+'/Default-375w-667h@2x-s.png')
        if not (img.size == (750,1334)):
            clipResizeImg(img,750,1334,dstimgpath+'/Default-375w-667h@2x.png')
        else:
            print 'default clip completed,terminated'
        os.system('rm -r '+dstimgpath+'/Default-375w-667h@2x-s.png')
        
        #	640 * 960     Default@2x-1.png
        img = Image.open(oriimgpath)
        clipResizeImg(img,640,960,dstimgpath+'/Default@2x-s.png')
        img = Image.open(dstimgpath+'/Default@2x-s.png')
        if not (img.size == (640,960)):
            clipResizeImg(img,640,960,dstimgpath+'/Default@2x.png')
        else:
            print 'default clip completed,terminated'
        os.system('rm -r '+dstimgpath+'/Default@2x-s.png')
        
        #	640 * 1136    Default-568h@2x-1.png
        img = Image.open(oriimgpath)
        clipResizeImg(img,640,1136,dstimgpath+'/Default-568h@2x-s.png')
        img = Image.open(dstimgpath+'/Default-568h@2x-s.png')
        if not (img.size == (640,1136)):
            clipResizeImg(img,640,1136,dstimgpath+'/Default-568h@2x.png')
        else:
            print 'default clip completed,terminated'
        os.system('rm -r '+dstimgpath+'/Default-568h@2x-s.png')


