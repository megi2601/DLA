import glob
from PIL import Image

def make_gif(frame_folder):
    frames = [Image.open(image) for image in sorted(glob.glob(f"{frame_folder}/*.PNG"))]
    frame_one = frames[0]
    frame_one.save("1.gif", format="GIF", append_images=frames,
               save_all=True, duration=10, loop=0)
    
if __name__ == "__main__":
    make_gif("C:\SymulacjeKomputerowe\lab3_DLA\gif")