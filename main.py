from Classes.Estruturas import *
import math


def produtoEscalar(v1,v2):
    return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)

def norma(v1):
  return math.sqrt(math.pow(v1.x) + math.pow(v1.y) + math.pow(v1.z))

def main():  
    data = "My data read from the Web"
    print(data)

if __name__ == "__main__":
    main()