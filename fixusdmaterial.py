bl_info = {
    "name": "Fix USD Material Import",
    "description": "Fix the UVMap name of an imported UDS Material.",
    "author": "Johnny Matthews",
    "version": (1, 0),
    "blender": (3, 5, 1),
    "location": "Search Menu",
    "category": "Material",
}

import bpy


def main(context):
    for m in bpy.data.materials:
        if m.node_tree != None:
            for n in m.node_tree.nodes:
                if n.type == 'UVMAP':
                    if n.uv_map == "st":
                        n.uv_map = "UVMap"


class FixUSDMaterialOperator(bpy.types.Operator):
    """Fix Imported USD Material"""
    bl_idname = "material.fixusdimport"
    bl_label = "Fix USD Imported Materials"


    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(FixUSDMaterialOperator.bl_idname, text=FixUSDMaterialOperator.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(FixUSDMaterialOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()
