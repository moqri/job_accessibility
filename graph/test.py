
# Get the default router
# Could also be called: router = otp.getRouter('paris')
#router = otp.getRouter()

# Create a default request for a given time
req = otp.createRequest()
req.setDateTime(2015, 1, 15, 10, 00, 00)
req.setMaxTimeSec(1800)

# Create a regular and rectangular n x n grid of points
grid = otp.createGridPopulation(33, 34, 84, 85, 100, 100)

print type(grid)
