FROM jupyter/pyspark-notebook:latest

LABEL Vincent Nijs "radiant@rady.ucsd.edu"

USER root

# update permissions as root
RUN fix-permissions /etc/jupyter/ \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "${JULIA_PKGDIR}" \
    && fix-permissions "${HOME}"

USER "${NB_UID}"

WORKDIR "${HOME}"
