.PHONY: srpm

srpm:
	mkdir -p $(outdir)
	tar czf $(outdir)/evolution-on.tar.gz \
	  --exclude-vcs --exclude=./.copr \
	  --transform 's,^\.,evolution-on-master,' .
	rpmbuild -bs \
	  --define "_sourcedir $(outdir)" \
	  --define "_srcrpmdir $(outdir)" \
	  evolution-on.spec
