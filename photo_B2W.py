import cv2
import os

def inverse(image):
	h, w, channels = image.shape[0:3]
	for row in range(h):
		for col in range(w):
			for c in range(channels):
				pixel = image[row,col,c]
				image [ row, col, c] = 255-pixel
	return image

print("請輸入要截圖的資料夾名稱：")
file_name = str(input())

path='D://Users//xkllkx//Desktop//all_program//photo_B2W//'+file_name+"//" #這就是欲進行檔名更改的檔案路徑，路徑的斜線是為/，要留意下！
#D:\Users\xkllkx\Desktop\all_program\photo_B2W\direct
#路径不能包含中文
#图片是否在该路径下，确保路径没有问题。
#路径中单斜杠'\'替换成双斜杠'\\'或'//'或‘/’。

files=os.listdir(path)
#print('files') #印出讀取到的檔名稱，用來確認自己是不是真的有讀到

n=0 #設定初始值
for i in files: #因為資料夾裡面的檔案都要重新更換名稱
	oldname=path+files[n] #指出檔案現在的路徑名稱，[n]表示第n個檔案
	#print(oldname)
	newname=path+file_name+"_"+str(n+1)+'.png' #在本案例中的命名規則為：年份+ - + 次序，最後一個.wav表示該檔案的型別
	#print(newname)

	os.rename(oldname,newname)
	print(files[n]+' >>> '+file_name+"_"+str(n+1)+'.png') #印出原名與更名後的新名，可以進一步的確認每個檔案的新舊對應

	#opencv讀不到中文檔名，所以須先改名
	#圖片格式要對，例如：jpg、png
	png = cv2.imread(newname) #imread讀取 imwrite儲存
	
	#png = inverse(png) #副函式也可以用
	png = 255 - png

	cv2.imwrite(newname,png) #imread讀取 imwrite儲存
	
	print(file_name+"_"+str(n+1)+'.png'+' B2W完成')

	print("------------------------")
	n=n+1 #當有不止一個檔案的時候，依次對每一個檔案進行上面的流程，直到更換完畢就會結束

	#待更新:
	#自定義截圖範圍
	#重複檔名會出錯
