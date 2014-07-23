import sublime, sublime_plugin

# class TrimHiddenCharacters(sublime_plugin.EventListener):
#     def on_pre_save(self, view):
#         if view.settings().get("trim_hidden_characters_on_save") == True:
#             hidden_characters = view.find_all(u"\u8203")
#             hidden_characters.reverse()
#             edit = view.begin_edit()
#             for r in hidden_characters:
#                 view.erase(edit, r)
#             view.end_edit(edit)
