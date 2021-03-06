import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL


accel_gyro = LSM6DS(board.STEMMA_I2C())
mag = LIS3MDL(board.STEMMA_I2C())


acceleration = accel_gyro.acceleration
gyro = accel_gyro.gyro
magnetic = mag.magnetic
print(
    "Acceleration: X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} m/s^2".format(*acceleration))
print("Gyro          X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} rad/s".format(*gyro))
print("Magnetic      X:{0:7.2f}, Y:{1:7.2f}, Z:{2:7.2f} uT".format(*magnetic))
