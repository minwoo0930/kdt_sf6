# os 모듈 - 디렉터리, 파일 등의 자원을 제어하는 모듈
import os


file_path = os.chdir("C:/kdt_sf6/pyworks/modules") #디렉터리 경로
dir = os.popen('dir') #'dir' 명령으로 열기 - 목록 보기
print(dir.read())

print(os.listdir(file_path)) #파일들을 리스트로 저장함

