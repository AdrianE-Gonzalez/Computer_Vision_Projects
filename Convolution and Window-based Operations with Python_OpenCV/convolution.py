import math

def build_mask(image,mask):

    m,n=mask.size()
    M,N=image.size()

    m2= math.floor(m/2)
    n2= math.floor(n/2)

    for i in range(m2,M-m2):
        for j in range(n2,N-n2):
            sum=0.0
            for x in range(-m2,m2):
                for y in range(-n2,n2):
                    sum+=h[x+m2][y+n2].f[i+x][j+y]

            g[i][j]=clip[sum]

    return 0