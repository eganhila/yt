import yt

# Load the dataset.
ds = yt.load("GalaxyClusterMerger/fiducial_1to3_b0.273d_hdf5_plt_cnt_0175")

# Create a data object that represents the whole box.
ad = ds.h.all_data()

# This is identical to the simple phase plot, except we supply 
# the fractional=True keyword to divide the profile data by the sum. 
plot = yt.PhasePlot(ad, "density", "temperature", "cell_mass",
                 weight_field=None, fractional=True)

# Set a new title for the colorbar since it is now fractional.
plot.z_title["cell_mass"] = r"$\mathrm{Mass}\/\mathrm{fraction}$"

# Reset the plot so it is redrawn when we save the image.
plot.reset_plot()

# Save the image.
# Optionally, give a string as an argument
# to name files with a keyword.
plot.save()
