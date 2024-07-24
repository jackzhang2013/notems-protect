import webview
import bug

class API():
    def protect(self, overlay_text, target_name="target", force_editing=True):
        bug.protect(overlay_text=overlay_text, target_name=target_name, force_editing=force_editing)
        # print(targetName, force_editing)

def main():
    api = API()
    webview.create_window('note.ms protector', 'file://D:/notems-protector/web/index.html', js_api=api)
    webview.start()

if __name__ == '__main__':
    main()