from talon import Context, actions


context = Context()


@context.action_class("user")
class NoiseActions:
    def on_pop():
        actions.mouse_click()

    def on_hiss(start: bool):
        # TODO: Maybe use audio cues to notify user of premature release?
        if start:
            actions.mouse_drag()
        else:
            actions.mouse_release()
