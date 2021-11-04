
import bpy


class BaseOperator:
    def func(context):
        Objects_and_Distance = []
        Camera = objects_in_collection = bpy.data.collections["Collection"].objects["Camera"].location
        for Collection in bpy.data.collections:
            for objects in Collection.objects:
                x = objects
                location1 = bpy.data.collections[f"{Collection.name}"].objects[f"{x.name}"].location
                distance = (location1 - Camera).magnitude
                #list for further use
                e1 = {
                    "Object Name" : x.name,
                    "Distance" : distance
                }
                Objects_and_Distance.append(e1)
                #change the comparison to change the Distance threshold the decimate
                #anything further than 10m will be decimated
                if(distance > 10):
                    bpy.context.view_layer.objects.active = bpy.data.collections['Collection'].objects[f"{x.name}"]
                    bpy.ops.object.modifier_add(type='DECIMATE')
                    #change the multiply value to increase the decimation intesity
                    Decimate_Ratio = 1
                    Decimate_Ratio = 1 - (distance * 0.3 / 10) # +  user input
                    bpy.context.object.modifiers["Decimate"].ratio = Decimate_Ratio
                    print(Decimate_Ratio)
                    

class SimpleOperator(bpy.types.Operator , BaseOperator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        BaseOperator.func(context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SimpleOperator)



def unregister():
    bpy.utils.unregister_class(SimpleOperator)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.simple_operator()