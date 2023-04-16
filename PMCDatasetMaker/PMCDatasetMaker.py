'''
import os
import zipfile
import shutil
 
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except:
                shutil.copy2(s, d)
        else:
            shutil.copy2(s, d)
 
path = 'R:/MCDataset/addmods/'
for filename in os.listdir(path):
    if filename[-4:] == '.jar':
        with zipfile.ZipFile(path + filename, 'r') as zip_file:
            k = zip_file.namelist()
            if 'assets/' in k:
                if os.path.exists('R:/MCDataset/buf'):
                    shutil.rmtree('R:/MCDataset/buf')
                os.mkdir('R:/MCDataset/buf')
                zip_file.extractall('R:/MCDataset/buf')
                flist = os.listdir('R:/MCDataset/buf/assets')
                for fna in flist:
                    if os.path.exists('R:/MCDataset/buf/assets/' + fna + '/textures'):
                        os.system("xcopy R:\\MCDataset\\buf\\assets\\" + fna + "\\textures\\*.png " + "R:\\MCDataset\\newadd16\\" + fna + "\\textures " + "/H /Y /R /S")
                if os.path.exists('R:/MCDataset/buf'): 
                    shutil.rmtree('R:/MCDataset/buf')
 
 
import os
from PIL import Image
 
path = "R:/MCDataset/add16"
 
def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, 'deleted')
 
for root, dirs, files in os.walk(path):
    for file in files:
        imname = os.path.join(root, file)
        try:
            if Image.open(imname).size == (32, 32):
                os.remove(imname)
        except:
            a = 0
            
path = "R:/MCDataset/add16"
del_empty_dirs(path)
 
 
 
import os
path = r"R:/MCDataset/all32"
path2 = r"R:/MCDataset/16"
f = open('list.txt', 'w')
 
folders = os.listdir(path)
folders2 = os.listdir(path2)
 
for fol in folders:
    if fol not in folders2:
        f.write(fol + '\n')
f.close()
 
 
 
'''
'''
import os #режет блоки на куски
from PIL import Image
 
def create_path(path):
    if "\\" in path:
        path = path[:path.rfind('\\')]
    elif ".png" in path:
        path = path[:path.rfind('/')]
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            try:
                os.makedirs(path)
            except Exception as e:
                print(e)
 
path = r"R:/MCDataset/16n/"
path2 = r"R:/MCDataset/16c/"

for root, dirs, files in os.walk(path):
    for f in files:
        pname = os.path.join(root, f)
        image = Image.open(pname)
        orig = image
        x, y = image.size
        divider = x
        counter = 0
        if x > y:
            if x % y == 0:
                divider = y
                while x != 0:
                    cr = image.crop((0, 0, divider, divider))
                    p = path2 + pname[17:-4] + "_" + str(counter) + ".png"
                    create_path(p)
                    cr.save(p)
                    image = image.crop((divider, 0, x, y))
                    x, y = image.size
                    counter += 1
            else:
                orig.save(path2 + "e/" + f)
        else:
            if y % x == 0:
                while y != 0:
                    cr = image.crop((0, 0, divider, divider))
                    p = path2 + pname[17:-4] + "_" + str(counter) + ".png"
                    create_path(p)
                    cr.save(p)
                    image = image.crop((0, divider, x, y))
                    x, y = image.size
                    counter += 1
            else:
                orig.save(path2 + "e/" + f)
'''

'''
import os #для обрезки диффектных обрезков
from PIL import Image
 
def create_path(path):
    if "\\" in path:
        path = path[:path.rfind('\\')]
    elif ".png" in path:
        path = path[:path.rfind('/')]
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            try:
                os.makedirs(path)
            except Exception as e:
                print(e)
 
path = r"R:/MCDataset/32e/"
path2 = r"R:/MCDataset/32n/"

for root, dirs, files in os.walk(path):
    for f in files:
        pname = os.path.join(root, f)
        image = Image.open(pname)
        orig = image
        x, y = image.size
        counter = 0
        if x > y:
            if x % 2 == 0:
                divider = x / 2
                while x != 0:
                    cr = image.crop((0, 0, divider, divider))
                    p = path2 + pname[17:-4] + "_" + str(counter) + ".png"
                    cr.save(p)
                    image = image.crop((divider, 0, x, y))
                    x, y = image.size
                    counter += 1
            else:
                create_path(path2 + "e/")
                orig.save(path2 + "e/" + f)
        else:
            if y % 2 == 0:
                divider = y / 2
                while y != 0:
                    cr = image.crop((0, 0, divider, divider))
                    p = path2 + pname[17:-4] + "_" + str(counter) + ".png"
                    cr.save(p)
                    image = image.crop((0, divider, x, y))
                    x, y = image.size
                    counter += 1
            else:
                create_path(path2 + "e/")
                orig.save(path2 + "e/" + f)
'''


''' 
from PIL import Image
import os
import shutil
 
path1 = r"R:/MCDataset/16t/"
path2 = r"R:/MCDataset/32p/"
 
def create_path(path):
    if "\\" in path:
        path = path[:path.rfind('\\')]
    elif ".png" in path:
        path = path[:path.rfind('/')]
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as e:
            try:
                os.makedirs(path)
            except Exception as e:
                print(e)
 
for root, dirs, files in os.walk(path2):
    for f in files:
        pname = os.path.join(root, f)
        p1 = "R:/MCDataset/16p/" + pname[17:]
        p2 = "R:/MCDataset/16n/" + pname[17:]
        create_path(p2)
        shutil.copyfile(p1, p2)
for root, dirs, files in os.walk(path1):
    for f in files:
        pname = os.path.join(root, f)
        try:
            image = Image.open(pname)
        except:
            p1 = "R:/MCDataset/16p/" + pname[17:]
            create_path(p1)
            shutil.copyfile(pname, p1)
            break
        rgba_im = image.convert('RGBA')
        flag = True
        for x in range(16):
            r, g, b, a = rgba_im.getpixel((x, 0))
            if a == 0:
                flag = False
                break
        if flag:
            for x in range(16):
                r, g, b, a = rgba_im.getpixel((x, 15))
                if a == 0:
                    flag = False
                    break
        if flag:
            for y in range(16):
                r, g, b, a = rgba_im.getpixel((0, y))
                if a == 0:
                    flag = False
                    break
        if flag:
            for y in range(16):
                r, g, b, a = rgba_im.getpixel((15, y))
                if a == 0:
                    flag = False
                    break
        if not flag:
            p1 = "R:/MCDataset/16p/" + pname[17:]
            create_path(p1)
            image.save(p1)
            image.close()
            p1 = "R:/MCDataset/32p/" + pname[17:]
            create_path(p1)
            shutil.copyfile(path2 + pname[17::], p1)
        elif flag:
            p1 = "R:/MCDataset/16c/" + pname[17:]
            create_path(p1)
            image.save(p1)
            image.close()
            p1 = "R:/MCDataset/32c/" + pname[17:]
            create_path(p1)
            shutil.copyfile(path2 + pname[17::], p1)
           
 
 
 
 
 
import os
import shutil
 
path = "R:/MCDataset/16r/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        if ".png" in f:
            nf = root[17::]
            pos = nf.find("\\")
            while pos != -1:
                if pos != len(nf):
                    nf = nf[:nf.find("\\")] + "_" + nf[nf.find("\\") + 1:] + "_"
                else:
                    nf = nf[:nf.find("\\")] + "_"
                pos = nf.find("\\")
            nf += f
            p = "R:/MCDataset/16f/" + nf
            shutil.copyfile(root + "\\" + f, p)
 
 
 
 
import os
import shutil
 
for root, dirs, files in os.walk("R:/MCDataset/32c/"):
    for f in files:
        pname = os.path.join(root, f)
        p1 = "R:/MCDataset/16c/" + f
        p = "R:/MCDataset/16f/" + root[17::] + "\\" + f
        shutil.copyfile(pname, p)
 


import os #вычисляет значение того, насколько хорошо текстуры коннектятся
from PIL import Image
 
path = "R:/MCDataset/16c/v/"
 
minc = 1000
maxc = 0
avc = 0
bc = 0
 
for root, dirs, files in os.walk(path):
    for f in files:
        counter = 0
        pname = os.path.join(root, f)
        image = Image.open(pname)
        rgb_im1 = image.convert('RGBA')
        dp = 0
        for y in range(16):
            r1, g1, b1, a1 = rgb_im1.getpixel((0, y))
            r2, g2, b2, a2 = rgb_im1.getpixel((15, y))
            dp += (abs((r1 * 1.0) / 255 - (r2 * 1.0) / 255) + abs((g1 * 1.0) / 255 - (g2 * 1.0) / 255) + abs((b1 * 1.0) / 255 - (b2 * 1.0) / 255) + abs((a1 * 1.0) / 255 - (a2 * 1.0) / 255)) / 4.0
        bc += 1
        dp /= 16
        minc = min(minc, dp)
        maxc = max(maxc, dp)
        avc += dp



import os #скопировать текстуры, которые хорошо коннектятся
from PIL import Image
import shutil

path = "R:/MCDataset/16c/"
path2 = "R:/MCDataset/16f/"
for root, dirs, files in os.walk(path):
    for f in files:
        counter = 0
        pname = os.path.join(root, f)
        try:
            image = Image.open(pname)
            rgb_im2 = image.convert('RGBA')
            dp1 = 0
            dp2 = 0
            for y in range(16):
                r1, g1, b1, a1 = rgb_im2.getpixel((0, y))
                r2, g2, b2, a2 = rgb_im2.getpixel((15, y))
                if a1 != 0 and a2 != 0:
                    dp1 += (abs((r1 * 1.0) / 255 - (r2 * 1.0) / 255) + abs((g1 * 1.0) / 255 - (g2 * 1.0) / 255) + abs((b1 * 1.0) / 255 - (b2 * 1.0) / 255) + abs((a1 * 1.0) / 255 - (a2 * 1.0) / 255)) / 4.0
                    counter += 1
            dp1 /= counter
            counter = 0
            for x in range(16):
                r1, g1, b1, a1 = rgb_im2.getpixel((x, 0))
                r2, g2, b2, a2 = rgb_im2.getpixel((x, 15))
                if a1 != 0 and a2 != 0:
                    dp2 += (abs((r1 * 1.0) / 255 - (r2 * 1.0) / 255) + abs((g1 * 1.0) / 255 - (g2 * 1.0) / 255) + abs((b1 * 1.0) / 255 - (b2 * 1.0) / 255) + abs((a1 * 1.0) / 255 - (a2 * 1.0) / 255)) / 4.0
                    counter +=1
            dp2 /= counter
            image.close()
            if dp1 < 0.014:
                if dp2 < 0.014:
                    shutil.copyfile(pname, path2 + "f/" + f)
                else:
                    shutil.copyfile(pname, path2 + "v/" + f)
            elif dp2 < 0.014:
                shutil.copyfile(pname, path2 + "h/" + f)
            else:
                shutil.copyfile(pname, path2 + "another/" + f)
        except:
            image.close()
            shutil.copyfile(pname, path2 + "another/" + f)
'''


'''
import os #обрезает прозрачные рамки
from PIL import Image
import shutil
 
path = "R:/MCDataset/16m/"
path1 = "R:/MCDataset/16n/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        counter = 0
        pname = os.path.join(root, f)
        try:
            image = Image.open(pname)
            w, h = image.size
            rgb_im = image.convert('RGBA')
            frame = True
            while frame:
                for x in range(w):
                    r, g, b, a = rgb_im.getpixel((x, 0))
                    if a != 0:
                        frame = False
                        break
                if frame:
                    image = image.crop((0, 1, w, h))
                    h -= 1
                    rgb_im = image.convert('RGBA')
            frame = True
            while frame:
                for x in range(w):
                    r, g, b, a = rgb_im.getpixel((x, h - 1))
                    if a != 0:
                        frame = False
                        break
                if frame:
                    h -= 1
                    image = image.crop((0, 0, w, h))
                    rgb_im = image.convert('RGBA')
            frame = True
            while frame:
                for y in range(h):
                    r, g, b, a = rgb_im.getpixel((0, y))
                    if a != 0:
                        frame = False
                        break
                if frame:
                    image = image.crop((1, 0, w, h))
                    w -= 1
                    rgb_im = image.convert('RGBA')
            frame = True
            while frame:
                for y in range(h):
                    r, g, b, a = rgb_im.getpixel((w - 1, y))
                    if a != 0:
                        frame = False
                        break
                if frame:
                    w -= 1
                    image = image.crop((0, 0, w, h))
            image.save(path1 + f)
            image.close()
        except:
            shutil.copyfile(pname, path1 + "e/" + f)
'''



'''
#import shutil # Удаляет одинаковые файлы
from tkinter import Tk
import os
import hashlib
from pathlib import Path
from tqdm import tqdm

Tk().withdraw()
file_path = "R:\\MCDataset\\16rr\\"
print(file_path + ":")
list_of_files = os.walk(file_path)
unique_files = dict()
counter = 0
for root, folders, files in list_of_files:
    for file in tqdm(files):
        pname = os.path.join(root, file)
        file_path = Path(os.path.join(root, file))
        Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
        if Hash_file not in unique_files:
            unique_files[Hash_file] = file_path
            #shutil.copyfile(file_path, "R:/MCDataset/32n/" + file)
        else:
            counter += 1
            #shutil.copyfile(file_path, "R:/MCDataset/32n/e/" + str(counter) + "_" + file)
            os.remove(file_path)
            #shutil.copyfile(file_path, "R:/MCDataset/16n/e/" + file)
'''


'''
import os #убирает одноцветные текстуры
from PIL import Image
import shutil
 
path = "R:/MCDataset/16m/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        counter = 0
        pname = os.path.join(root, f)
        image = Image.open(pname)
        w, h = image.size
        rgb_im = image.convert('RGBA')
        oc = True
        r1, g1, b1, a1 = rgb_im.getpixel((0, 0))
        for x in range(w):
            for y in range(h):
                r2, g2, b2, a2 = rgb_im.getpixel((x, y))
                if (r1 != r2) or (g1 != g2) or (b1 != b2) or (a1 != a2):
                    oc = False
                    shutil.copyfile(path + f, "R:/MCDataset/16n/" + f)
                    break
            if not oc:
                break
        if (oc):
            image.save("R:/MCDataset/16n/e/" + f)    
        image.close()
'''


'''
import os #убирает текстуры без альфаслоя
from PIL import Image
import shutil
 
path = "R:/MCDataset/16a/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        counter = 0
        pname = os.path.join(root, f)
        image = Image.open(pname)
        w, h = image.size
        rgb_im = image.convert('RGBA')
        oc = True
        for x in range(w):
            for y in range(h):
                r, g, b, a = rgb_im.getpixel((x, y))
                if a != 255:
                    oc = False
                    shutil.copyfile(path + f, "R:/MCDataset/16n/" + f)
                    break
            if not oc:
                break
        if (oc):
            image.save("R:/MCDataset/16n/e/" + f)    
        image.close()
'''


'''
import os #сортирует изображения на с прозрачным фоном и все, у всех удаляет фон, прозрачные копирует, копирует маску
from PIL import Image
import numpy as np
import cv2

pm = "32"
path = "R:/MCDataset/" + pm + "/"

def make_mask(path):
    img_array = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2RGBA)
    h,w,c = img_array.shape
    A_img_array = np.zeros ((h, w, 3), dtype = np.uint8)
    A_img_array[:, :, 0] = img_array[:, :, 3]
    A_img_array[:, :, 1] = img_array[:, :, 3]
    A_img_array[:, :, 2] = img_array[:, :, 3]
    cv2.imwrite("R:/MCDataset/" + pm + "m/" + path[16::], A_img_array)

def remove_transparency(im):
    bg_colour = (255, 255, 255)
    alpha = im.convert('RGBA').split()[-1]
    bg = Image.new("RGBA", im.size, bg_colour + (255,))
    bg.paste(im, mask = alpha)
    return bg

for root, dirs, files in os.walk(path):
    for f in files:
        pname = os.path.join(root, f)
        image = Image.open(pname)
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            image.save("R:/MCDataset/" + pm + "a/" + f) #изображения без альфа канала
            make_mask(pname) #изображения в виде альфа канала, преобразованного в чёрно-белый
            image = remove_transparency(image)
        else:
            image.save("R:/MCDataset/" + pm + "f/" + f) #изображения изначально без альфаканала
        image.save("R:/MCDataset/" + pm + "r/" + f) #все изображения без альфа канала, в том числе с удалённым
        image.close()
'''



'''
import os #склеивает изображения 1 в 4
from PIL import Image
 
path = "R:/MCDataset/16m/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        pname = os.path.join(root, f)
        image = Image.open(pname)
        w, h = image.size
        W = 2 * w
        H = 2 * h
        img = Image.new('RGBA', (W, H))
        rgb_im = image.convert('RGBA')
        img.paste(rgb_im, (0,0))
        img.paste(rgb_im, (0,h))
        img.paste(rgb_im, (w,0))
        img.paste(rgb_im, (w,h))
        img.save("R:/MCDataset/16n/" + f)    
        img.close()
'''


'''
import os #добавляет в датасет перевёрнутые и отзеркаленые изображения
from PIL import Image
mpath = "16"
path = "R:/MCDataset/" + mpath + "m/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        pname = os.path.join(root, f)
        image = Image.open(pname)
        for i in range(4):
            img = image
            image.save("R:/MCDataset/" + mpath + "mm/" + f[:-4] + "_o_" + str(i) + ".png")
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image.save("R:/MCDataset/" + mpath + "mm/" + f[:-4] + "_h_" + str(i) + ".png")
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image.save("R:/MCDataset/" + mpath + "mm/" + f[:-4] + "_vh_" + str(i) + ".png")
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image.save("R:/MCDataset/" + mpath + "mm/" + f[:-4] + "_v_" + str(i) + ".png")
            image = image.rotate(90)
        image.close()
#os.system('shutdown -s')
'''


'''
import os #рандомизирует файлы
import shutil
import random
import glob
from tqdm import tqdm

path = "R:/MCDataset/r/32n/"
counter = 0
cf = len(glob.glob(path + '*.png'))
rlist = []
cfm = cf - 1
for i in range(cf):
    rlist.append(i)
for i in range(cf):
    r = random.randint(0, cfm)
    rlist[r], rlist[i] = rlist[i], rlist[r]
for root, dirs, files in os.walk(path):
    for f in tqdm(files):
        pname = os.path.join(root, f)
        shutil.copyfile(pname, "R:/MCDataset/r/16n/" + str(rlist[counter]) + ".png")
        shutil.copyfile("R:/MCDataset/r/32/" + f, "R:/MCDataset/r/32n/" + str(rlist[counter]) + ".png")
        counter += 1
'''


'''
import os #делит датасет на валидационный и тренировочный
import shutil
import glob
from tqdm import tqdm

print("m:\n")
path = "R:/MCDataset/m/16/"
cf = len(glob.glob(path + '*.png'))
pers = 10 #сколько процентов валидационных данных кладём
sizeofval = int(cf / pers)
for root, dirs, files in os.walk(path):
    for i in tqdm(range(sizeofval)):
        for f in files:
            pname = os.path.join(root, f)
            shutil.move(pname, "R:/MCDataset/m/16v/" + f)
            shutil.move("R:/MCDataset/m/32/" + f, "R:/MCDataset/m/32v/" + f)

print("a:\n")
path = "R:/MCDataset/a/16/"
cf = len(glob.glob(path + '*.png'))
pers = 10 #сколько процентов валидационных данных кладём
c = 0
sizeofval = int(cf / pers)
for root, dirs, files in os.walk(path):
    for f in tqdm(files):
        if c < sizeofval:
            pname = os.path.join(root, f)
            shutil.move(pname, "R:/MCDataset/a/16v/")
            shutil.move("R:/MCDataset/a/32/" + f, "R:/MCDataset/a/32v/")
        else:
            exit(0)
        c += 1

print("r:\n")
path = "R:/MCDataset/r/16/"
cf = len(glob.glob(path + '*.png'))
pers = 10 #сколько процентов валидационных данных кладём
c = 0
sizeofval = int(cf / pers)
for root, dirs, files in os.walk(path):
    for f in tqdm(files):
        if c < sizeofval:
            pname = os.path.join(root, f)
            shutil.move(pname, "R:/MCDataset/r/16v/")
            shutil.move("R:/MCDataset/r/32/" + f, "R:/MCDataset/r/32v/")
        else:
            exit(0)
        c += 1
'''



'''
import os #множит слишком маленькие изображения
from PIL import Image

path = "R:/MCDataset/32m/"
path2 = "R:/MCDataset/16m/"
 
for root, dirs, files in os.walk(path):
    for f in files:
        pname = os.path.join(root, f)
        image = Image.open(pname)
        image2 = Image.open(path2 + f)
        w, h = image.size
        while w < 64 or h < 64:
            w2, h2 = image2.size
            img = Image.new('RGBA', (2 * w, 2 * h))
            img2 = Image.new('RGBA', (2 * w2, 2 * h2))
            rgb_im = image.convert('RGBA')
            rgb_im2 = image2.convert('RGBA')
            img.paste(rgb_im, (0,0))
            img.paste(rgb_im, (0,h))
            img.paste(rgb_im, (w,0))
            img.paste(rgb_im, (w,h))
            img2.paste(rgb_im2, (0,0))
            img2.paste(rgb_im2, (0,h2))
            img2.paste(rgb_im2, (w2,0))
            img2.paste(rgb_im2, (w2,h2))
            image = img
            image2 = img2
            w, h = image.size
        image2.save("R:/MCDataset/16n/" + f)  
        image.save("R:/MCDataset/32n/" + f)
        image.close()
        image2.close()
'''


'''
import shutil # Копирует парные изображения
import os
from tqdm import tqdm
counter = 0
print("\nr:\n")
for root, dirs, files in os.walk("R:/MCDataset/32r/"):
    for f in tqdm(files):
        if counter > 815466:
            if os.path.exists("R:/MCDataset/16r/" + f):
                shutil.copyfile("R:/MCDataset/32r/" + f, "R:/MCDataset/32rr/" + f)
                shutil.copyfile("R:/MCDataset/16r/" + f, "R:/MCDataset/16rr/" + f)
        counter += 1
'''


'''
import cv2#обработка картинок уже для нейронки
import numpy as np
import os
from multiprocessing import Pool
from os import path as osp
from tqdm import tqdm

from basicsr.utils import scandir


def main():
    opt = {}
    opt['n_thread'] = 8
    opt['compression_level'] = 0
    opt['input_folder'] = 'R:/MCDataset/16r'
    opt['save_folder'] = 'R:/MCDataset/16rr'
    opt['crop_size'] = 32
    opt['step'] = 16
    opt['thresh_size'] = 0
    extract_subimages(opt)

def extract_subimages(opt):
    input_folder = opt['input_folder']
    save_folder = opt['save_folder']
    if not osp.exists(save_folder):
        os.makedirs(save_folder)
        print(f'mkdir {save_folder} ...')
    img_list = list(scandir(input_folder, full_path=True))
    pbar = tqdm(total=len(img_list), unit='image', desc='Extract')
    pool = Pool(opt['n_thread'])
    for path in img_list:
        pool.apply_async(worker, args=(path, opt), callback=lambda arg: pbar.update(1))
    pool.close()
    pool.join()
    pbar.close()
    print('All processes done.')


def worker(path, opt):
    crop_size = opt['crop_size']
    step = opt['step']
    thresh_size = opt['thresh_size']
    img_name, extension = osp.splitext(osp.basename(path))

    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    h, w = img.shape[0:2]
    h_space = np.arange(0, h - crop_size + 1, step)
    if h - (h_space[-1] + crop_size) > thresh_size:
        h_space = np.append(h_space, h - crop_size)
    w_space = np.arange(0, w - crop_size + 1, step)
    if w - (w_space[-1] + crop_size) > thresh_size:
        w_space = np.append(w_space, w - crop_size)

    index = 0
    for x in h_space:
        for y in w_space:
            index += 1
            cropped_img = img[x:x + crop_size, y:y + crop_size, ...]
            cropped_img = np.ascontiguousarray(cropped_img)
            cv2.imwrite(
                osp.join(opt['save_folder'], f'{img_name}_s{index:03d}{extension}'), cropped_img,
                [cv2.IMWRITE_PNG_COMPRESSION, opt['compression_level']])
    process_info = f'Processing {img_name} ...'
    return process_info


if __name__ == '__main__':
    main()
'''
'''
import os #создаёт файлы для QD
import glob
from tqdm import tqdm

fp = open('prompt.txt', 'a')
fv = open('valImages.txt', 'a')
ft = open('trainImages.txt', 'a')
path = "R:/QuickDrowDataset/"
pers = 10 #сколько процентов валидационных данных кладём
for root, dirs, files in os.walk(path):
    for d in tqdm(dirs):
        mpath = path + d
        cf = len(glob.glob(mpath + '\\*.gif'))
        sizeofval = int(cf / pers)
        for i in range(sizeofval):
            fname = "\n" + d + "\\" + str(i) + ".gif"
            fp.write(fname + "#0\t" + d + " .")
            fv.write(fname)
        for i in range(sizeofval, cf):
            fname = "\n" + d + "\\" + str(i) + ".gif"
            fp.write(fname + "#0\t" + d + " .")
            ft.write(fname)
fp.close()
fv.close()
ft.close()
'''

import numpy
import cv2
from PIL import Image
import requests
import json

chat_id = "-1001661093241"
TOKEN = "5572539231:AAGWOteLeewnSrIqNqjZ6Yvx0uPlmqbvq_w"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def send_document_to_tg(req_text, tgfile):
    req = requests.post(req_text, files = tgfile)
    content = req.content.decode("utf8")
    content_json = json.loads(content)
    message_id = str(content_json["result"]["message_id"])
    return message_id

def make_mask(img, path_to_save):
    img_array = numpy.array(img)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2RGBA)
    h, w, c = img_array.shape
    A_img_array = numpy.zeros((h, w, 3), dtype = numpy.uint8)
    A_img_array[:, :, 0] = img_array[:, :, 3]
    A_img_array[:, :, 1] = img_array[:, :, 3]
    A_img_array[:, :, 2] = img_array[:, :, 3]
    cv2.imwrite(path_to_save, A_img_array)
    im_buf_arr = cv2.imencode(".png", A_img_array)[1]
    b_data = im_buf_arr.tobytes()
    return b_data

mask = make_mask(Image.open("img1.png"), "picture.png")
message_id = send_document_to_tg(URL + "sendDocument?&reply_to_message_id=" + "77" + "caption=C маской&chat_id=" + chat_id, {"document": ("mask_" + str(0) + ".png", mask)})