

class parts:
    def UI_set(self, UI_operation):
        data = UI_operation

        def size_update(self, width_size, height_size):
            pass

        def view(self, all_elements, frame_user_select):
            tk_image = data.operation["out"]["output_video_image"]["CentralRole"].type_preview(all_elements, data.operation, frame_user_select, data.canvas_size)
            data.tk_picture(tk_image)
            """
            image_pil = Image.fromarray(view_picture)  # RGBからPILフォーマットへ変換
            img_resize = image_pil
            if resize:
                img_resize = image_pil.resize((data.canvas_size[0], data.canvas_size[1]))
            image_tk = ImageTk.PhotoImage(image_pil)  # ImageTkフォーマットへ変換
            """

        data.update_event = size_update

        return data
