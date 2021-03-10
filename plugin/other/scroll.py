class CentralRole:
    def main(self, data, direction):

        data.direction = int(direction)

        data.new_diagram("back")
        data.new_diagram("view")

        data.edit_diagram_fill("back", True)
        data.edit_diagram_fill("view", False)

        data.edit_diagram_color("back", "#555555")
        data.edit_diagram_color("view", "#00cccc")

        data.edit_diagram_fill("view", True, direction=1-data.direction)

        # 百分率は0~100ではなく0~1でやること、100でやられるとしんどい

        data.drawing_area = [0, 0]
        # territory左上を0,0とした基準で、描画可能範囲を記入します
        # 配列0番 : territory+space起点からパーセント起点まで 実数表示!
        # 配列1番 : territory+space起点からterritory終点-spaceまで 実数表示!

        data.pos_drawing_area = [0, 0]  # 実数表示!
        # data.drawing_areaを元にした座標の移動範囲を計算します
        # 計算方法は (1 - サイズ割合)をかけることです

        data.percent_range = [0, 0]
        # 配列0番 : territory起点からパーセント中心まで 割合表示！
        # 配列1番 : パーセントのサイズ 割合表示！

        data.click_distance = 0
        # クリックした場所から,パーセント起点まで、どれだけの距離があるかどうかを計算 実数表示！

        data.brack_space = 0
        # data.directionによって指定された方向の両側に,data.brack_spaceのスペースを作ります
        # これにより描画禁止領域をdiagramに設定することができます

        data.scroll_sta_event = None
        data.scroll_event = None
        data.scroll_end_event = None

        data.lr_edit = False

        data.scroll_minimum_value_px = 1  # 1px設定

        def set_scroll_minimum_value_px(select):
            data.scroll_minimum_value_px = select

        def set_lr_edit(select):
            data.lr_edit = select

        data.set_lr_edit = set_lr_edit
        data.set_scroll_minimum_value_px = set_scroll_minimum_value_px

        def set_scroll_event(func):
            data.scroll_event = func

        def set_scroll_sta_event(func):
            data.scroll_sta_event = func

        def set_scroll_end_event(func):
            data.scroll_end_event = func

        data.set_scroll_event = set_scroll_event
        data.set_scroll_event(data.event_not_func)

        data.set_scroll_sta_event = set_scroll_sta_event
        data.set_scroll_sta_event(data.event_not_func)

        data.set_scroll_end_event = set_scroll_end_event
        data.set_scroll_end_event(data.event_not_func)

        def run_scroll_event():
            if not str(type(data.scroll_event)) == "<class 'function'>":
                return
            data.scroll_event(data.percent_range)

        def run_scroll_sta_event():
            if not str(type(data.scroll_event)) == "<class 'function'>":
                return
            data.scroll_sta_event(data.percent_range)

        def run_scroll_end_event():
            if not str(type(data.scroll_event)) == "<class 'function'>":
                return
            data.scroll_end_event(data.percent_range)

        #print("scroll class ID", data)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        def percent_calculation():

            data.drawing_area[0] = data.brack_space
            data.drawing_area[1] = data.edit_territory_size()[data.direction] - data.brack_space

            data.drawing_area_length = data.drawing_area[1] - data.drawing_area[0]

            data.pos_drawing_area[0] = data.drawing_area[0]
            data.pos_drawing_area[1] = data.drawing_area_length * (1 - data.percent_range[1]) + data.drawing_area[0]

            return

        def stopper():

            if data.percent_range[0] < 0:
                edit_percent_percentage(position=0)

            if data.percent_range[0] > 1:
                edit_percent_percentage(position=1)

            #print("割合情報", data.percent_range)

            return

        def edit_size(x=None, y=None, space=None):

            if not space is None:
                data.brack_space = space

            data.edit_territory_size(x=x, y=y)
            percent_calculation()
            edit_percent_percentage()
            data.territory_draw()

        def __edit_percent_movement_size(size):
            if size < data.scroll_minimum_value_px:
                size = data.scroll_minimum_value_px
                # print("検知A")

            if size > data.drawing_area_length:
                size = data.drawing_area_length
                # print("検知B")

            sta_xy = [None, None]
            sta_xy[data.direction] = size

            data.edit_diagram_size("view", x=sta_xy[0], y=sta_xy[1])

            data.percent_range[1] = size / data.drawing_area_length if data.drawing_area_length != 0 else 0

            data.territory_draw()

            percent_calculation()
            run_scroll_event()

            stopper()

        def __edit_percent_movement(position):  # 移動量で設定する
            #print("移動量", position)

            area_pos = position - data.pos_drawing_area[0]  # 現在地より描画開始地点を引いた値

            if area_pos < 0:
                area_pos = 0

            if area_pos > data.drawing_area_length:
                area_pos = data.drawing_area_length

            sta_xy = [None, None]
            sta_xy[data.direction] = area_pos + data.pos_drawing_area[0]  # 最終描画確定位置

            data.edit_diagram_position("view", x=sta_xy[0], y=sta_xy[1])
            data.territory_draw()

            percent_calculation()
            #print(position, data.pos_drawing_area[0])

            pos_drawing_area_length = data.pos_drawing_area[1] - data.pos_drawing_area[0]

            data.percent_range[0] = area_pos / (pos_drawing_area_length) if pos_drawing_area_length != 0 else 0

            #print("割合計算", data.percent_range, position - data.pos_drawing_area[0], data.pos_drawing_area[1] - data.pos_drawing_area[0])

            run_scroll_event()
            # 割合を算出します
            stopper()

        def edit_percent_percentage(position=None, size=None):  # 割合で設定する
            data.percent_range = data.common_control.xy_compilation(data.percent_range, x=position, y=size)

            percent_calculation()

            #print(data.drawing_area, data.pos_drawing_area)

            pos_length = data.pos_drawing_area[1] - data.pos_drawing_area[0]
            size_length = data.drawing_area[1] - data.drawing_area[0]

            sta = pos_length * data.percent_range[0] + data.pos_drawing_area[0]
            end = size_length * data.percent_range[1]

            sta_xy = [None, None]
            end_xy = [None, None]

            sta_xy[data.direction] = sta
            end_xy[data.direction] = end

            data.edit_diagram_position("view", x=sta_xy[0], y=sta_xy[1])
            data.edit_diagram_size("view", x=end_xy[0], y=end_xy[1])

            stopper()

            run_scroll_event()

            data.territory_draw()

            # print("割合で変更")

            return

        data.click_flag = False

        def click_start(event):

            ##print(data.canvas_data.territory[data.te_name].diagram["view"].position[0], data.canvas_data.canvas.bbox(data.common_control.get_tag_name(data.te_name, "view")))
            # data.operation["error"].action(message="test")

            data.click_flag = True
            data.mouse_sta, data.mouse_touch_sta, data.diagram_join_sta = data.get_diagram_contact("view")
            data.view_pos_sta = data.edit_diagram_position("view")[data.direction]
            data.view_size_sta = data.edit_diagram_size("view")[data.direction]
            # クリックした場所から,パーセント起点まで、どれだけの距離があるかどうかを計算
            # 計算の基準は描画開始地点  data.drawing_area[0] : "# 配列0番 : territory起点からパーセント起点まで 実数表示!" です
            # つまりterritory起点+spaceからここまでどのぐらいの距離があるかどうかを判定します

            run_scroll_sta_event()

        def click_mov(event):
            if not data.click_flag:
                return
            now_mouse, _, data.diagram_join = data.get_diagram_contact("view")

            now_mov = now_mouse[data.direction] - data.mouse_sta[data.direction]

            if data.lr_edit and data.mouse_touch_sta[data.direction][0]:

                size = data.view_size_sta-now_mov
                pos = data.view_pos_sta+now_mov

                if size < data.scroll_minimum_value_px and 0 < now_mov:
                    #print("反応P 差分", data.scroll_minimum_value_px - size)
                    pos -= (data.scroll_minimum_value_px - size)

                if now_mov < 0 and pos < data.pos_drawing_area[0]:
                    return

                __edit_percent_movement_size(size)  # posとsizeを同時に変更する場合は先にsizeをおかないとダメらしい
                __edit_percent_movement(pos)

            elif data.lr_edit and data.mouse_touch_sta[data.direction][1]:
                __edit_percent_movement_size(data.view_size_sta+now_mov)

            elif data.diagram_join_sta[2]:  # 範囲内に入っているか確認します この関数に限りmotion判定でwindowに欠けているので必要です
                pos = data.view_pos_sta + now_mov
                __edit_percent_movement(pos)
                percent_calculation()

        def click_end(event):

            data.click_flag = False

            data.mouse_sta, data.mouse_touch_sta, data.diagram_join_sta = data.get_diagram_contact("view", del_mouse=True)
            data.mouse, _, data.diagram_join = data.get_diagram_contact("view", del_mouse=True)

            run_scroll_end_event()

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        edit_size(x=0, y=0, space=0)
        edit_percent_percentage(position=0.00, size=0.5
                                )
        data.add_diagram_event("view", "Button-1", click_start)
        data.window_event_data["add"]("Motion", click_mov)
        data.add_diagram_event("view", "ButtonRelease-1", click_end)

        data.territory_draw()

        data.edit_size = edit_size
        data.percent_calculation = percent_calculation
        data.edit_percent_percentage = edit_percent_percentage
        #data.edit_percent_movement = edit_percent_movement

        return data
