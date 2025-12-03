import numpy as np
import matplotlib.pyplot as plt

def plot_projectile_motion():
    # Constants
    INITIAL_VELOCITY = 25.0  # m/s
    TOTAL_TIME = 3.0  # seconds
    TARGET_DISTANCE = 45.0  # meters
    GRAVITY = 9.8  # m/s²
    NUM_POINTS = 300  # Number of points for smooth plotting
    
    try:
        # Calculate launch angle
        cos_theta = TARGET_DISTANCE / (INITIAL_VELOCITY * TOTAL_TIME)
        if abs(cos_theta) > 1:
            raise ValueError("Invalid parameters: Target cannot be reached with given velocity and time")
            
        launch_angle = np.arccos(cos_theta)  # radians
        
        # Calculate initial velocity components
        velocity_x = INITIAL_VELOCITY * np.cos(launch_angle)
        velocity_y = INITIAL_VELOCITY * np.sin(launch_angle)
        
        # Time array
        time_points = np.linspace(0, TOTAL_TIME, NUM_POINTS)
        
        # Calculate position at each time point
        horizontal_position = velocity_x * time_points
        vertical_position = velocity_y * time_points - 0.5 * GRAVITY * time_points**2
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(horizontal_position, vertical_position, 'b-', linewidth=2)
        plt.title('Projectile Motion Trajectory')
        plt.xlabel('Horizontal Distance (m)')
        plt.ylabel('Vertical Position (m)')
        plt.grid(True)
        plt.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
        plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
        plt.show()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    plot_projectile_motion()
plt.title("Projectile Motion of Water Stream")
plt.grid(True)
plt.show()