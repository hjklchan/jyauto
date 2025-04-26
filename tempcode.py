# if __name__ == '__main__':
# 下载 https://objects.githubusercontent.com/github-production-release-asset-2e65be/47605084/9c763d61-6460-41e1-945c-eb0e6ef09a95?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250425%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250425T053118Z&X-Amz-Expires=300&X-Amz-Signature=b63c162052f9ef57a4532ef33108fc4b2ef6bf1c63b0b5ea742828d7659f71db&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3Dtesseract-ocr-w64-setup-5.4.0.20240606.exe&response-content-type=application%2Foctet-stream
# 下载 https://raw.githubusercontent.com/tesseract-ocr/tessdata/main/chi_sim.traineddata
# pytesseract.pytesseract.tesseract_cmd = r'S:\Tesseract-OCR\tesseract.exe'

# # # 获取 app 窗口
# # appWindow = gw.getWindowsWithTitle("DeepL")[0]
# # # 激活窗口
# # appWindow.activate()

# screenshot = ImageGrab.grab()
# screenshot.save("screenshot.png")

# img_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
# data = pytesseract.image_to_data(img_cv, "chi_sim", config='--psm 6 --oem 3', output_type=pytesseract.Output.DICT)
# print("你好")
# print(data)

