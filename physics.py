import math
def jump(x0,y0,v0,a0,theta,time):
    '''
    Jump takes the character's x0,y0,v0,a0, the jump angle from horizontal, and
    amount of time and returns the xt and yt for that time
    '''
    if theta <= 90:
        v0x = v0 * math.cos(theta)
        v0y = v0 * math.sin(theta)
    elif theta > 90:
        theta -= 90
        v0x = v0 * math.sin(theta)
        v0y = v0 * math.cos(theta)
    xpos = x0 + (v0x*time) + (1/2)*a0*(time**2)
    ypos = y0 + (v0y*time) - (1/2)*9.8*(time**2)
    return xpos,ypos