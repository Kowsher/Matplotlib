import matplotlib.pyplot as plt
import numpy as np

x_surf, y_surf = np.meshgrid(np.linspace(X[:,0].min(), X[:,0].max(), 100),np.linspace(X[:,1].min(), X[:,0].max(), 100))
onlyX = pd.DataFrame({'Age': x_surf.ravel(), 'Weight': y_surf.ravel()})
onlyXD = np.matrix(onlyX.values, dtype=np.float32)
fittedY=il.predict(onlyXD)

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0],X[:,1],Y[:,0],c='red', marker='o', alpha=0.5)
#ax.scatter(X[:,0],X[:,1],pred_y[:,0],c='g', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='b', alpha=0.3)
ax.set_xlabel('Age')
ax.set_ylabel('Weight')
ax.set_zlabel('BP')
plt.show()
