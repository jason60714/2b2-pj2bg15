# Cango gearUtils-0.9.js Spur Gears
from browser import document as doc
from browser import html
from browser import window
import browser.timer
import math

canvas = html.CANVAS(width = 600, height = 400)
canvas.id = "cango_gear"
brython_div = doc["brython_div2"]
brython_div <= canvas
canvas = doc["cango_gear"]
# 此程式採用 Cango Javascript 程式庫繪圖, 因此無需 ctx
#ctx = canvas.getContext("2d")
cango = window.Cango.new
path = window.Path.new
creategeartooth = window.createGearTooth.new
circle = window.circle.new
svgsegs = window.SVGsegs.new
# 經由 Cango 轉換成 Brython 的 cango, 指定將圖畫在 id="cango_gear" 的 canvas 上
cgo = cango("cango_gear")

######################################
# 畫正齒輪輪廓
#####################################
def cangoGear(n, m, pa, x=0, y=0, color="#606060"):
    # n 為齒數
    #n = 17
    # pa 為壓力角
    #pa = 25
    # m 為模數, 根據畫布的寬度, 計算適合的模數大小
    # Module = mm of pitch diameter per tooth
    #m = 0.8*canvas.width/n
    # pr 為節圓半徑
    pr = n*m/2 # gear Pitch radius
    # generate gear data
    data = creategeartooth(m, n, pa)
    toothSVG = svgsegs(data)
    toothSVG.rotate(180/n) # rotate gear 1/2 tooth to mesh
    # 單齒的齒形資料經過旋轉後, 將資料複製到 gear 物件中
    one = toothSVG.dup()
    # 利用單齒輪廓旋轉, 產生整個正齒輪外形
    for i in range(1, n):
        newSVG = one.rotate(360*i/n)
        toothSVG = toothSVG.appendPath(newSVG)
    # 建立軸孔
    # add axle hole, hr 為 hole radius
    hr = 0.6*pr # diameter of gear shaft
    shaft = circle(hr)
    shaftSVG = svgsegs(shaft)
    spurSVG = toothSVG.appendPath(shaftSVG)
    gear = path(spurSVG, {"x": x, "y": y, "strokeColor": color})
    return gear

# 設定兩齒齒數
n1 = 84
n2 = 18
n3 = 99
# 使用 80% 的畫布寬度
m = 0.8*canvas.width/((n1+n2+n3))
# 設定共同的壓力角
pa = 25
# n 齒輪的節圓半徑
pr1 = n1*m/2
# n2 齒輪的節圓半徑
pr2 = n2*m/2
pr3 = n3*m/2
cx = canvas.width/2
cy = canvas.height/2
# Determine the coord of the middle gears
mcx = cx + (pr1-pr3)
mcy = cy
# 建立 gears
gear1 = cangoGear(n1, m, pa, color="red")
gear2 = cangoGear(n2, m, pa, color="green")
gear3 = cangoGear(n3, m, pa, color="blue")
deg = math.pi/180
rotate_speed = 0

def draw():
    global rotate_speed
    rotate_speed += 5*deg
    cgo.clearCanvas()
    theta1 = 0+rotate_speed
    gear1.rotate(theta1)
    gear1.translate(mcx-(pr1+pr2), mcy)
    cgo.render(gear1)
    
    theta2 = 180+(360/n2/2)-(rotate_speed)*n1/n2
    gear2.rotate(theta2)
    gear2.translate(mcx, mcy)
    cgo.render(gear2)
  
    theta3 = 180+(360/n3/2)+(180+(360/n2/2))*n2/n3+(rotate_speed*n1/n2)*(n2/n3)
    gear3.rotate(theta3)  
    gear3.translate(mcx+(pr2+pr3), mcy)
    cgo.render(gear3)

browser.timer.set_interval(draw, 2)