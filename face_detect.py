# extract and plot each detected face in a photograph
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
import os

# draw each face separately
def draw_faces(filename, result_list):
	try:
		# load the image
		data = pyplot.imread(filename)
		# plot each face as a subplot
		for i in range(len(result_list)):
			# get coordinates
			x1, y1, width, height = result_list[i]['box']
			x2, y2 = x1 + width, y1 + height
			# define subplot
			# pyplot.subplot(1, len(result_list), i+1)
			pyplot.axis('off')
			# plot face
			pyplot.imshow(data[y1:y2, x1:x2])
			# show the plot
			pyplot.savefig("E:/Kroop AI/horse2zebra/downloads/em_final/"+filename.split("/")[-1].split(".")[0]+"_"+str(i)+".jpg")
	except:
		pass

path = r'E:/Kroop AI/horse2zebra/downloads/elon musk/'
for pic in os.listdir(path):
	try:
		filename = path+pic
		print(filename)
		# load image from file
		pixels = pyplot.imread(filename)
		# create the detector, using default weights
		detector = MTCNN()
		# detect faces in the image
		faces = detector.detect_faces(pixels)
		# print(faces)
		# display faces on the original image
		draw_faces(filename, faces)
	except:
		pass