import random
def capture_sharpness():
    data = random.uniform(0, 1)
    data = round(data, 2)
    return data

def take_picture():
    global picture
    picture = True

def adjust_focus(current_sharpness):
    global previous_sharpness, picture
    if current_sharpness > previous_sharpness:
        print("Putar fokus ke kanan")
    elif current_sharpness < previous_sharpness:
        print("Putar fokus ke kiri")
    else:
        print("Ambil gambar")
        take_picture()

    previous_sharpness = current_sharpness

def run_autofocus():
    global picture
    while picture == False:
        current_sharpness = capture_sharpness()
        adjust_focus(current_sharpness)

if __name__ == "__main__":
    previous_sharpness = float(input('Masukan ketajaman : '))
    previous_sharpness = round(previous_sharpness,2)
    picture = False
    run_autofocus()
