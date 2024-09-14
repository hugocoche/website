import matplotlib.pyplot as plt


# plt.rc('figure',figsize=(6.4,4.8))
# sont les dimensions de la fenêtre graphique par défaut, on pourra l'ajuster en fonction de nos besoin
def mon_theme(
    fig,
    Ax,
    nrows=1,
    ncols=1,
    titre="",
    titre_fontsize=15,
    couleur_titre="darkred",
    titre_bold=True,
    xlabelsize=10,
    ylabelsize=10,
    xlabel="x",
    ylabel="y",
    xlabelcolor="black",
    ylabelcolor="black",
    xlabelpad=0,
    ylabelpad=0,
    xfontstyle="italic",
    yfontstyle="italic",
    legende_differente=True,
    show_legende_a_droite=True,
    legend_fontsize=7,
    couleur_des_abscisses="midnightblue",
    couleur_des_ordonnees="midnightblue",
    couleur_des_axes="black",
    couleur_fond_graph="lightgrey",
    couleur_bord_fenêtre="black",
    couleur_fond_fenêtre="lightgrey",
    show_grid=False,
    scatter_edgecolors="black",
    grid_color="grey",
    alpha_grid=0.5,
    style_grid="--",
    fancybox=True,
    legend_title="Légende :",
    ancre_legende_horizontale=1.0,
    ancre_legende_verticale=0.91,
    couleur_fond_legende="lightgrey",
    couleur_bord_legende="black",
    loc_si_legende_interieure=1,
    marge_droite_graph=0.83,
    hauteur_graph=1.0,
):
    plt.suptitle(titre, size=titre_fontsize, color=couleur_titre, fontweight=titre_bold)
    plt.rcParams["axes.edgecolor"] = couleur_des_axes
    plt.rcParams["axes.facecolor"] = couleur_fond_graph
    plt.rcParams["figure.edgecolor"] = couleur_bord_fenêtre
    plt.rcParams["figure.facecolor"] = couleur_fond_fenêtre
    plt.rcParams["xtick.labelcolor"] = couleur_des_abscisses
    plt.rcParams["ytick.labelcolor"] = couleur_des_ordonnees
    plt.rcParams["scatter.edgecolors"] = scatter_edgecolors
    if ncols != 1 and nrows != 1:
        for i in range(nrows):
            for j in range(ncols):
                if show_grid:
                    Ax[i, j].grid(
                        color=grid_color, alpha=alpha_grid, linestyle=style_grid
                    )
                Ax[i, j].set_xlabel(
                    xlabel,
                    color=xlabelcolor,
                    size=xlabelsize,
                    labelpad=xlabelpad,
                    fontstyle=xfontstyle,
                )
                Ax[i, j].set_ylabel(
                    ylabel,
                    color=ylabelcolor,
                    size=ylabelsize,
                    labelpad=ylabelpad,
                    fontstyle=yfontstyle,
                )
    elif ncols == 1 and nrows != 1:
        for i in range(nrows):
            for j in range(ncols):
                if show_grid:
                    Ax[i].grid(color=grid_color, alpha=alpha_grid, linestyle=style_grid)
                Ax[i].set_xlabel(
                    xlabel,
                    color=xlabelcolor,
                    size=xlabelsize,
                    labelpad=xlabelpad,
                    fontstyle=xfontstyle,
                )
                Ax[i].set_ylabel(
                    ylabel,
                    color=ylabelcolor,
                    size=ylabelsize,
                    labelpad=ylabelpad,
                    fontstyle=yfontstyle,
                )
    elif ncols != 1 and nrows == 1:
        for i in range(nrows):
            for j in range(ncols):
                Ax[j].grid(color=grid_color, alpha=alpha_grid, linestyle=style_grid)
                Ax[j].set_xlabel(
                    xlabel,
                    color=xlabelcolor,
                    size=xlabelsize,
                    labelpad=xlabelpad,
                    fontstyle=xfontstyle,
                )
                Ax[j].set_ylabel(
                    ylabel,
                    color=ylabelcolor,
                    size=ylabelsize,
                    labelpad=ylabelpad,
                    fontstyle=yfontstyle,
                )
    else:
        if show_grid:
            Ax.grid(color=grid_color, alpha=alpha_grid, linestyle=style_grid)
        Ax.set_xlabel(
            xlabel,
            color=xlabelcolor,
            size=xlabelsize,
            labelpad=xlabelpad,
            fontstyle=xfontstyle,
        )
        Ax.set_ylabel(
            ylabel,
            color=ylabelcolor,
            size=ylabelsize,
            labelpad=ylabelpad,
            fontstyle=yfontstyle,
        )
    if show_legende_a_droite:
        # Collectez les éléments de légende et les étiquettes de légende de chaque sous-graphique
        handles = []
        labels = []
        if nrows != 1 and ncols != 1:
            if legende_differente:
                for i in range(nrows):
                    for j in range(ncols):
                        h, l = Ax[i, j].get_legend_handles_labels()
                        handles.extend(h)
                        labels.extend(labels)
            else:
                h, l = Ax[0, 0].get_legend_handles_labels()
                handles.extend(h)
                labels.extend(l)
        elif nrows == 1 and ncols != 1:
            if legende_differente:
                for j in range(ncols):
                    h = Ax[j].get_legend_handles_labels()
                    handles.extend(h)
                    labels.extend(l)
            else:
                h, l = Ax[0].get_legend_handles_labels()
                handles.extend(h)
                labels.extend(l)
        elif nrows != 1 and ncols == 1:
            if legende_differente:
                for i in range(nrows):
                    h, l = Ax[i].get_legend_handles_labels()
                    handles.extend(h)
                    labels.extend(l)
            else:
                h, l = Ax[0].get_legend_handles_labels()
                handles.extend(h)
                labels.extend(l)
        else:
            h, l = Ax.get_legend_handles_labels()
            handles.extend(h)
            labels.extend(l)
        # Créez une légende globale
        fig.legend(
            handles,
            labels,
            fancybox=fancybox,
            fontsize=legend_fontsize,
            title=legend_title,
            bbox_to_anchor=(ancre_legende_horizontale, ancre_legende_verticale),
            facecolor=couleur_fond_legende,
            edgecolor=couleur_bord_legende,
        )
    else:
        if nrows != 1 and ncols != 1:
            for i in range(nrows):
                for j in range(ncols):
                    Ax[i, j].legend(
                        loc=loc_si_legende_interieure, fontsize=legend_fontsize
                    )
        elif nrows == 1 and ncols != 1:
            for j in range(ncols):
                Ax[j].legend(loc=loc_si_legende_interieure, fontsize=legend_fontsize)
        elif nrows != 1 and ncols == 1:
            for i in range(nrows):
                Ax[i].legend(loc=loc_si_legende_interieure, fontsize=legend_fontsize)
        else:
            Ax.legend(loc=loc_si_legende_interieure, fontsize=legend_fontsize)
    return fig.tight_layout(rect=(0, 0.0, marge_droite_graph, hauteur_graph))


# si marge_droite_graph alors les graph prendront 70% du graph en partant de la gauche
# rect(left,bottom,right,top) règle les marges


def mon_themev2(
    fig,
    Ax,
    nrows=1,
    ncols=1,
    titre="",
    titre_fontsize=15,
    couleur_titre="darkred",
    titre_bold=True,
    xlabelsize=10,
    ylabelsize=10,
    xlabel="x",
    ylabel="y",
    xlabelcolor="black",
    ylabelcolor="black",
    xlabelpad=0,
    ylabelpad=0,
    xfontstyle="italic",
    yfontstyle="italic",
    legende_differente=True,
    show_legende_a_droite=True,
    legend_fontsize=7,
    couleur_des_abscisses="midnightblue",
    couleur_des_ordonnees="midnightblue",
    couleur_des_axes="black",
    couleur_fond_graph="lightgrey",
    couleur_bord_fenêtre="black",
    couleur_fond_fenêtre="lightgrey",
    show_grid=False,
    scatter_edgecolors="black",
    grid_color="grey",
    alpha_grid=0.5,
    style_grid="--",
    fancybox=True,
    legend_title="Légende :",
    ancre_legende_horizontale=1.0,
    ancre_legende_verticale=0.91,
    couleur_fond_legende="lightgrey",
    couleur_bord_legende="black",
    loc_si_legende_interieure=1,
    marge_droite_graph=0.83,
    hauteur_graph=1.0,
):
    plt.suptitle(titre, size=titre_fontsize, color=couleur_titre, fontweight=titre_bold)
    plt.rcParams["axes.edgecolor"] = couleur_des_axes
    plt.rcParams["axes.facecolor"] = couleur_fond_graph
    plt.rcParams["figure.edgecolor"] = couleur_bord_fenêtre
    plt.rcParams["figure.facecolor"] = couleur_fond_fenêtre
    plt.rcParams["xtick.labelcolor"] = couleur_des_abscisses
    plt.rcParams["ytick.labelcolor"] = couleur_des_ordonnees
    plt.rcParams["scatter.edgecolors"] = scatter_edgecolors

    for ax in Ax:
        if show_grid:
            ax.grid(color=grid_color, alpha=alpha_grid, linestyle=style_grid)
        ax.set_xlabel(
            xlabel,
            color=xlabelcolor,
            size=xlabelsize,
            labelpad=xlabelpad,
            fontstyle=xfontstyle,
        )
        ax.set_ylabel(
            ylabel,
            color=ylabelcolor,
            size=ylabelsize,
            labelpad=ylabelpad,
            fontstyle=yfontstyle,
        )

    if show_legende_a_droite:
        handles, labels = [], []
        for ax in Ax:
            h, l = ax.get_legend_handles_labels()
            handles.extend(h)
            labels.extend(l)
        fig.legend(
            handles,
            labels,
            fancybox=fancybox,
            fontsize=legend_fontsize,
            title=legend_title,
            bbox_to_anchor=(ancre_legende_horizontale, ancre_legende_verticale),
            facecolor=couleur_fond_legende,
            edgecolor=couleur_bord_legende,
        )
    else:
        for ax in Ax:
            ax.legend(loc=loc_si_legende_interieure, fontsize=legend_fontsize)

    return fig.tight_layout(rect=(0, 0.0, marge_droite_graph, hauteur_graph))
