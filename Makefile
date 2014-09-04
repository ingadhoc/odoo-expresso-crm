all: addons

design/crm_expresso.xmi: design/crm_expresso.zargo
	-echo "REBUILD crm_expresso.xmi from crm_expresso.zargo. I cant do it"

addons: crm_expresso

crm_expresso: design/crm_expresso.uml
	xmi2oerp -r -i $< -t addons -v 2

clean:
	# mv addons/README ./README_addons_clean
	# rm -rf addons/crm_expresso/*
	# mv README_addons_clean addons/README
	sleep 1
	touch design/crm_expresso.uml
