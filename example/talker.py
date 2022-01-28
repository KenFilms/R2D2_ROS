import rospy
from std_msgs.msg import String
   
   
def r2d2():
   pub = rospy.Publisher('r2d2_hello', String, queue_size=10)
   rospy.init_node('r2d2', anonymous=True)
   rate = rospy.Rate(10) # 10h
      while not rospy.is_shutdown():
         r2d2_hello = "Hello world from R2." 
         rospy.loginfo(r2d2_hello)
         pub.publish(r2d2_hello)
         rate.sleep()

if __name__ == '__main__':
   try:
      r2d2()
      except rospy.ROSInterruptException:
         pass
