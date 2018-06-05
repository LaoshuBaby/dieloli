import core.winframe as winframe
import core.PyCmd as pycmd
import core.CacheContorl as cache

wframe = winframe.root

#按键监听绑定预设
def onWFrameListion():
    wframe.bind('<ButtonPress-1>', mouseLeftCheck)
    wframe.bind('<ButtonPress-3>',mouseRightCheck)
    wframe.bind('<Return>', winframe.send_input)
    wframe.bind('<KP_Enter>',winframe.send_input)
    wframe.bind('<Up>',keyUp)
    wframe.bind('<Down>',keyDown)

#鼠标左键事件
def mouseLeftCheck(event):
    if cache.wframeMouse['wFrameUp'] ==0:
        setWFrameUp(event)
    else:
        mouseCheckPush(event)

#鼠标右键事件
def mouseRightCheck(event):
    cache.wframeMouse['mouseRight'] = 1
    cache.textWait = 0
    if cache.wframeMouse['wFrameUp'] ==0:
        setWFrameUp(event)
    else:
        mouseCheckPush(event)

#键盘上键事件
def keyUp(event):
    while cache.inputPosition['position'] == 0:
        cache.inputPosition['position'] = len(cache.inputCache)
    while cache.inputPosition['position'] <= 21 and cache.inputPosition['position'] > 1:
        cache.inputPosition['position'] = cache.inputPosition['position'] - 1
        inpotId = cache.inputPosition['position']
        try:
            winframe.order.set(cache.inputCache[inpotId])
            break
        except KeyError:
            cache.inputPosition['position'] = cache.inputPosition['position'] + 1
    pass

#键盘下键事件
def keyDown(event):
    if cache.inputPosition['position'] > 0 and cache.inputPosition['position'] < len(cache.inputCache) - 1:
        try:
            cache.inputPosition['position'] = cache.inputPosition['position'] + 1
            inpotId = cache.inputPosition['position']
            winframe.order.set(cache.inputCache[inpotId])
        except KeyError:
            cache.inputPosition['position'] = cache.inputPosition['position'] - 1
    elif cache.inputPosition['position'] == len(cache.inputCache) - 1:
        cache.inputPosition['position'] = 0
        winframe.order.set('')
    pass

#逐字输出状态改变
def setWFrameUp(event):
    cache.wframeMouse['wFrameUp'] = 1
    cache.wframeMouse['wFrameLinesUp'] = 1

#鼠标点击状态
def mouseCheckPush(event):
    pycmd.focusCmd()
    if cache.wframeMouse['mouseLeaveCmd'] == 0:
        winframe.send_input()
        cache.wframeMouse['mouseLeaveCmd'] = 1
    else:
        pass