import hou
import pyperclip
import ast

def getBundles():
	getclip = pyperclip.paste()
	try:
		dict = ast.literal_eval(getclip)

		bdl_names = dict['bundles'].keys()

		for x in range(0, len(bdl_names)):
			name = bdl_names[x]
			nodes = dict['bundles'][name]
			if hou.nodeBundle(name):
				bdl = hou.nodeBundle(name)
			else:
				bdl = hou.addNodeBundle(name)

			# Add Same Nodes if exist
			for nd in nodes:
				if hou.node(nd):
					bdl.addNode(hou.node(nd))
				else:
					pass    

			# Set pattterns
			pattern = dict['bundle_pattern'][x]
			bdl.setPattern(pattern)    

			# Set filters
			# filter =  dict['bundle_filter'][x]
			# bdl.setFilter(filter)

	except:
		print 'Buffer filled not a bundle list data type, try copy to clipbord again'

def pasteBundles():
	
	bundles = []
	bundle_pattern = []
	bundle_filter = []

	for bdl in hou.nodeBundles():
	    bundle_pattern.append( bdl.pattern())
	    bundle_filter.append( bdl.filter())
	    nodes_list = []
	    for node in bdl.nodes():
	        nodes_list.append(node.path())
	    bundles.append( {bdl.name() : nodes_list } )

	bundle_elements = {x.keys()[0]: x.values()[0] for x in bundles}

	bundle_dict = {'bundles':bundle_elements, 'bundle_pattern':bundle_pattern, 'bundle_filter':str(bundle_filter)}

	pyperclip.copy(bundle_dict)