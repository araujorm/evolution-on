.PHONY: srpm

srpm:
	mkdir -p $(outdir)
	git archive --prefix=evolution-on-master/ --format=tar.gz HEAD \
	  -o $(outdir)/evolution-on.tar.gz
	rpmbuild -bs \
	  --define "_sourcedir $(outdir)" \
	  --define "_srcrpmdir $(outdir)" \
	  evolution-on.spec
