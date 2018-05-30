from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

#创建一个应用实例
app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle('Web页面中的JavaScript与QWebEngineView交互例子')
#创建一个垂直布局器
layout = QVBoxLayout()
win.setLayout(layout)
#创建一个QWebEngineView对象
view = QWebEngineView()
view.setHtml('''
<html>
<head>
<title>A demo Page</title>
<script language="javascript">
//获得输入的姓名，然后在页面中显示提交按钮 （这里注释不能用#）
    function completeAndReturnName() {
        var fname = document.getElementById('fname').value;
        var lname = document.getElementById('lname').value;
        var full = fname + ' ' + lname;

        document.getElementById('fullname').value = full;
        document.getElementById('submit-btn').style.display = 'block';
        return full;
    }
</script>
</head>

<body>
<form>
    <label for ="fname">First name:</label>
    <input type="text" name="fname" id="fname"></input>
    <br />
    <label for ="fname">Last name:</label>
    <input type="text" name="lname" id="lname"></input>
    <br />
    <label for ="fullname">Full name:</label>
    <input disabled type="text" name="fullname" id="fullname"></input>
    <br />
    <input style="display:none;"type="submit" id="submit-btn"></input>
</form>
</body>

</html>
'''
)
#创建一个按钮用于调用JavaScript代码
button = QPushButton('设置全名')

def js_callback(result):
    print(result)
def complete_name():
    view.page().runJavaScript('completeAndReturnName();', js_callback)
#按钮连接'complete_name'槽函数，当单击按钮时会触发信号
button.clicked.connect(complete_name)

#把QWebEngineView控件和按钮控件加载到layout布局中
layout.addWidget(view)
layout.addWidget(button)

#显示窗口和运行
win.show()
sys.exit(app.exec_())
