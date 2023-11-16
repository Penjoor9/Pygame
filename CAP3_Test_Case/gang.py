import unittest
import pygame
from pygame.locals import *

class TestPygame(unittest.TestCase):
   def setUp(self):
       pygame.init()
       self.width = 1000
       self.height = 600
       self.screen_res = (self.width, self.height)
       self.screen = pygame.display.set_mode(self.screen_res)
       self.blue = (250, 0, 0)
       self.pink = (0, 0, 0)
       self.ball_obj = pygame.draw.circle(surface=self.screen, color=self.blue, center=[100, 100], radius=40)
       self.speed = [1, 1]

   def test_screen_init(self):
       self.assertEqual(self.screen.get_width(), self.width)
       self.assertEqual(self.screen.get_height(), self.height)

   def test_circle_draw(self):
       self.assertEqual(self.ball_obj.center, [100, 100])
       self.assertEqual(self.ball_obj.radius, 40)
   def test_ball_move(self):
     old_position = self.ball_obj.center
     self.ball_obj = self.ball_obj.move(self.speed)
     self.assertEqual(self.ball_obj.center, [old_position[0] + self.speed[0], old_position[1] + self.speed[1]])

   def test_game_loop(self):
      while self.running:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                 self.running = False
          self.screen.fill(self.pink)
      self.assertEqual(self.running, False)


class TestPygame(unittest.TestCase):
 def setUp(self):
     pygame.init()
     self.width = 1000
     self.height = 600
     self.screen_res = (self.width, self.height)
     self.screen = pygame.display.set_mode(self.screen_res)
     self.blue = (250, 0, 0)
     self.pink = (0, 0, 0)
     self.ball_obj = pygame.draw.circle(surface=self.screen, color=self.blue, center=[100, 100], radius=40)
     self.speed = [1, 1]

 def test_ball_bounce(self):
     # Test if the ball bounces when it hits the left edge
     self.ball_obj.center = [0, 100]
     self.ball_obj = self.ball_obj.move(self.speed)
     self.assertEqual(self.ball_obj.center[0], 1)

     # Test if the ball bounces when it hits the right edge
     self.ball_obj.center = [self.width, 100]
     self.ball_obj = self.ball_obj.move(self.speed)
     

     # Test if the ball bounces when it hits the top edge
     self.ball_obj.center = [100, 0]
     self.ball_obj = self.ball_obj.move(self.speed)
     self.assertEqual(self.ball_obj.center[1], 1)

     # Test if the ball bounces when it hits the bottom edge
     self.ball_obj.center = [100, self.height]
     self.ball_obj = self.ball_obj.move(self.speed)
     
if __name__ == '__main__':
    unittest.main()

