import rembg 
from PIL import Image 


def remove_background(input_path,output_path):
    inp_file=open(input_path,'rb')
    out_file=open(output_path,'wb')

    inp_contents=inp_file.read()
    out_contents=rembg.remove(inp_contents)

    out_file.write(out_contents)



if __name__=="__main__":
    inp="./inp_images/skel.jpg"
    out="./out_images/skelnobg.png"
    remove_background(inp,out)