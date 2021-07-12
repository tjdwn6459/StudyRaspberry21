# 라이브러리 추가
import time
import RPi.GPIO as GPIO

s2 = 23# Raspberry pi PIN 23
s3 = 24# Raspberry pi PIN 24
out = 25# Raspberry pi PIN 25
NUM_CYCLES = 10

def read_value(a2,a3):
    GPIO.output(s2, a2)
    GPIO.output(s3,a3)
    # 센서 조정 시간 설정
    time.sleep(0.3)
    #전체주기 웨이팅
    start = time.time() # 현재 시간
    for impluse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(out, GPIO.FALLING)
    end = (time.time() - start)
    return NUM_CYCLES / end #색상결과리턴
   

def setup():
    ##GPIO 셋팅
    ##pass
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3,GPIO.OUT)
    GPIO.setup(out,GPIO.IN,pull_up_down=GPIO.PUD_UP) #센서결과 받기

def loop():
    ## 반복하면서 일처리 
    result = ''

    while True:
        red = read_value(GPIO.LOW,GPIO.LOW) # s2 low, s3 low
        time.sleep(0.1)##0.1second delay
        green = read_value(GPIO.HIGH,GPIO.HIGH)# s2 high, s3 high
        time.sleep(0.1)##0.1 second delay
        blue = read_value(GPIO.LOW,GPIO.HIGH) # s2 low, s3 high

        print('red={0}, green={1},blue={2}'.format(red,green,blue))
        time.sleep(1) 
if __name__ == '__main__':
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
