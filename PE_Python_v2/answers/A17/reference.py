import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
def gallery(folder):
    from pathlib import Path
    folder=Path(folder); folder.mkdir(parents=True,exist_ok=True)
    x=np.arange(1,5); y=np.array([2,5,3,6])
    fig,axes=plt.subplots(2,4,figsize=(12,6)); a=axes.ravel()
    a[0].plot(x,y,"o--",label="Diem",alpha=.7); a[0].legend(); a[0].set_xticks(x)
    a[1].scatter(x,y); a[2].bar(x,y); a[3].barh(x,y)
    a[4].axhline(3); a[5].axvline(2); a[6].fill(x,y); a[7].fill_between(x,y)
    for ax,title in zip(a,["line","scatter","bar","barh","axhline","axvline","fill","fill_between"]): ax.set_title(title)
    a[0].set(xlim=(0,5),ylim=(0,7),xlabel="Luot",ylabel="Diem"); a[0].annotate("Max",(4,6))
    fig.tight_layout(); fig.savefig(folder/"one.png",transparent=True); plt.close(fig)
    fig,a=plt.subplots(1,3,figsize=(9,3)); a[0].hist(y,bins=[0,3,5,7]); a[1].boxplot(y); a[2].violinplot(y)
    for ax,title in zip(a,["hist","box","violin"]): ax.set_title(title)
    fig.tight_layout(); fig.savefig(folder/"dist.png",transparent=True); plt.close(fig)
    X,Y=np.meshgrid(np.linspace(-2,2,12),np.linspace(-2,2,12)); Z=X**2+Y**2; U=-Y; V=X
    fig,axes=plt.subplots(2,4,figsize=(12,6)); a=axes.ravel()
    im=a[0].imshow(Z,cmap="viridis",origin="lower"); fig.colorbar(im,ax=a[0],label="Gia tri")
    a[1].pcolor(X,Y,Z); a[2].pcolormesh(X,Y,Z,shading="auto")
    contours=a[3].contour(X,Y,Z); a[3].clabel(contours)
    a[4].contourf(X,Y,Z); a[5].arrow(0,0,1,1,head_width=.15)
    a[6].quiver(X,Y,U,V); a[7].streamplot(X,Y,U,V)
    for ax,title in zip(a,["imshow","pcolor","pcolormesh","contour","contourf","arrow","quiver","streamplot"]):
        ax.set_title(title); ax.set_aspect("equal")
    fig.tight_layout(); fig.savefig(folder/"fields.png",transparent=True); plt.close(fig)
    return [str(folder/name) for name in ("one.png","dist.png","fields.png")]
