import os
import tkinter as tk
from string import capwords as caps

# _________________________________________________________________________
# Page Defaults
white = '#FFFFFF'
blue = '#296296'
red = '#e6375f'
orange = '#e95842'
green = '#269269'
active_blue = '#3e89d1'
active_red = '#ef6786'
active_orange = '#eb7d6c'
active_green = '#489c72'
logo_font = 'Arial, 16'
med_font = 'Arial, 15'
small_font = 'Arial, 11'
# _________________________________________________________________________


class App:
	def __init__(self, app):

		# Left and Right Columns
		self.left_col = tk.Frame(app, bg=blue)
		self.left_col.pack(side='left', fill='both')
		self.right_col = tk.Frame(app, bg=blue)
		self.right_col.pack(side='right', fill='both', expand=True)

		# _____________________ Inside Left Column ____________________________

		# Top Left
		self.top_l_frame = tk.Frame(self.left_col, bg=blue)
		self.top_l_frame.pack(fill='both')

		# Logo
		self.logo_label = tk.Label(self.top_l_frame, text='iNOTE', bg=blue,
			fg=white, font=logo_font)
		self.logo_label.pack(fill='both', ipadx=80, ipady=30)

		# ----------------------------------------------------

		# Middle Left
		self.mid_l_frame = tk.Frame(self.left_col, bg=white)
		self.mid_l_frame.pack(fill='both', expand=True)

		# Listbox
		self.listbox = tk.Listbox(self.mid_l_frame, bg=white, fg=blue, font=med_font,
			selectbackground=active_blue, selectforeground=white,
			border=0, highlightthickness=0)
		self.listbox.bind('<<ListboxSelect>>', self.item_clicked)
		self.listbox.pack(side='left', fill='both', padx=(5, 0), pady=5, expand=True)
		# Scroll-Bar
		yscroll = tk.Scrollbar(self.mid_l_frame, bg=white, highlightthickness=0,
			orient=tk.VERTICAL, border=0)
		yscroll.pack(side='right', fill='y', anchor='e')
		self.listbox.config(yscrollcommand=yscroll.set)

		# ----------------------------------------------------

		# Bottom Left
		self.btm_l_frame = tk.Frame(self.left_col, bg=blue)
		self.btm_l_frame.pack(side='bottom', fill='both')

		# New Note Button
		self.nn_btn = tk.Button(self.btm_l_frame, text='New Note', bg=blue, fg=white,
			activebackground=active_blue, activeforeground=white, font=med_font,
			relief='flat', highlightthickness=0, border=0, command=self.nn_title)
		self.nn_btn.pack(fill='both', ipady=10, expand=True)

		# _____________________ Inside Right Column ___________________________
		#                          * UNPACKED *

		# Getter
		self.title_data = tk.StringVar()

		# ----------------------------------------------------
		# Top Right

		# Top Right Frame
		self.top_r_frame = tk.Frame(self.right_col, bg=blue)

		# Title Frame
		self.title_frame = tk.Frame(self.top_r_frame, bg=blue)

		# Title Label
		self.title_label = tk.Label(self.title_frame, bg=blue, fg=white, font=med_font)

		# Title Entry-Field
		self.title_entry = tk.Entry(self.title_frame, bg=white, fg=blue, font=med_font,
			border=0, highlightthickness=0, textvariable=self.title_data)

		# Title Submit Button
		self.title_sub_btn = tk.Button(self.title_frame, bg=white, fg=blue, font=small_font,
			activebackground=active_blue, activeforeground=white,
			border=0, highlightthickness=0, relief='flat')

		# ----------------------------------------------------
		# Error Message Frame
		self.msg_frame = tk.Frame(self.right_col, bg=red)

		# Error Message Label
		self.msg_label = tk.Label(self.msg_frame, bg=red, fg=white, font=small_font)

		# ----------------------------------------------------
		# Middle Right

		# Middle Right Frame
		self.mid_r_frame = tk.Frame(self.right_col, bg=white)

		# Text-Area
		self.textarea = tk.Text(self.mid_r_frame, bg=white, fg=blue, font=med_font,
			border=0, highlightthickness=0)

		# ----------------------------------------------------
		# Bottom Right

		# Bottom Right Frame
		self.btm_r_frame = tk.Frame(self.right_col, bg=blue)

		# Delete Button
		self.del_btn = tk.Button(self.btm_r_frame, bg=red, fg=white,
			activebackground=active_red, activeforeground=white,
			font=med_font, relief='flat', border=0, highlightthickness=0)

		# Save Button
		self.save_btn = tk.Button(self.btm_r_frame, bg=green, fg=white,
			activebackground=active_green, activeforeground=white,
			font=med_font, relief='flat', border=0, highlightthickness=0)

		# ---------------------------------------------------

		# _________ Create directory, if not exists _________

		dirname = 'Notes/'
		if dirname != os.path.basename(dirname):
			try:
				os.mkdir(dirname)
			except:
				None

		# ________________ Populate List-Box ________________

		files_list = os.listdir('Notes/')
		try:
			for files in files_list:
				self.listbox.insert(0, files)
		except:
			None

	# _________________________________________________________________________
	def nn_title(self):

		# Disable "List-Box"
		self.listbox.config(state='disabled')

		# Re-direct "New Note Button"
		self.nn_btn.config(text='Cancel', bg=orange,
			activebackground=active_orange, command=self.reset_app)

		# Display "Title Frame" Content
		self.top_r_frame.pack(fill='both')
		self.title_frame.pack(ipady=31)
		self.title_label.config(text='Title:')
		self.title_label.pack(side='left')
		self.title_entry.pack(side='left', padx=5, ipady=1)
		self.title_entry.focus()
		self.title_sub_btn.config(text='Create', command=self.create_title)
		self.title_sub_btn.pack(side='left')

	# _________________________________________________________________________
	def create_title(self):

		# Getter
		get_title = self.title_data.get()
		self.get_title = caps(get_title)

		# If title entry field is empty, give error msg
		if self.get_title == '':
			self.msg_frame.pack(fill='both')
			self.msg_label.config(text='Please enter note title!')
			self.msg_label.pack(ipady=2)
		else:
			# Hide The "Error Message Frame"
			self.msg_frame.destroy()

			# Re-direct "New Note Button"
			self.nn_btn.config(text='New Note', bg=blue, state='disabled',
				activebackground=active_blue, command=self.nn_title)

			# Disable "Title Frame" Content
			self.title_entry.config(state='disabled')
			self.title_sub_btn.config(state='disabled')

			# Action Buttons
			self.btm_r_frame.pack(side='bottom', fill='both')
			# Delete Button
			self.del_btn.config(text='Delete ' + self.get_title, command=self.reset_app)
			self.del_btn.pack(side='left', fill='both', ipady=10, expand=True)
			# Save Button
			self.save_btn.config(text='Save ' + self.get_title, command=self.save_title)
			self.save_btn.pack(side='right', fill='both', ipady=10, expand=True)

	# _________________________________________________________________________
	def save_title(self):

		# Hide "Title Frame" Content
		self.title_frame.destroy()

		# ----------------------------------------------------
		# File-Path
		filename = 'Notes/' + self.get_title

		# Write to file
		try:
			with open(filename, 'w') as f_write:
				f_write.write('___ ' + self.get_title + ' ___\n\n')


		except:
			None
		# ----------------------------------------------------
		self.display_content()

	# _________________________________________________________________________
	def display_content(self):

		# Display "Text-Area"
		self.mid_r_frame.pack(fill='both', expand=True)
		self.textarea.config(height=12)
		self.textarea.pack(fill='both', padx=10, pady=10, expand=True)

		# ----------------------------------------------------
		# File
		file = self.get_title
		# File-Path
		filename = 'Notes/' + self.get_title

		# Check we have correct file
		if file == os.path.basename(filename):
			try:
				with open(filename) as f_read:
					show_content = f_read.read()


				self.textarea.insert(tk.END, show_content)
				self.textarea.focus()
			except:
				None
		# ----------------------------------------------------
		# Re-direct "Action Buttons"
		# Delete Button
		self.del_btn.config(text='Delete ' + self.get_title, command=self.del_file)
		# Save Button
		self.save_btn.config(text='Update ' + self.get_title, command=self.update_note)

	# _________________________________________________________________________
	def del_file(self):

		# Clear "Text-Area"
		self.textarea.delete(1.0, tk.END)

		# ----------------------------------------------------
		# File
		file = self.get_title
		# File-Path
		filename = 'Notes/' + self.get_title

		# Check we have the correct file
		if file == os.path.basename(filename):
			# Delete File
			try:
				os.remove(filename)
			except:
				None
		# ----------------------------------------------------
		self.reset_app()

	# _________________________________________________________________________
	def update_note(self):

		# Grab content from "Text-Area"
		get_textarea = self.textarea.get(1.0, tk.END)

		# ----------------------------------------------------
		# File
		file = self.get_title
		# File-Path
		filename = 'Notes/' + self.get_title

		# Check we have correct file
		if file == os.path.basename(filename):
			# Write to file
			try:
				with open(filename, 'w') as f_write:
					f_write.write(get_textarea + '\n')


			except:
				None
		# ----------------------------------------------------
		self.reset_app()

	# _________________________________________________________________________
	def item_clicked(self, *args):

		# Clear "Text-Area"
		self.textarea.delete(1.0, tk.END)

		# Re-direct "New Note Button"
		self.nn_btn.config(text='Close', bg=orange,
			activebackground=active_orange, command=self.reset_app)

		# ----------------------------------------------------
		# Use selected item in listbox to determine file-name
		selected = self.listbox.curselection()
		if selected:
			# ----------------------------------------------------
			selected = int(selected[0])
			item = self.listbox.get(selected)

			if item == os.path.basename('Notes/' + str(item)):
				# Read File
				try:
					with open('Notes/' + str(item)) as f_read:
						show_content = f_read.read()


					# Display "Text-Area"
					self.mid_r_frame.pack(fill='both', expand=True)
					self.textarea.config(height=12)
					self.textarea.pack(fill='both', padx=10, pady=10, expand=True)
					self.textarea.insert(tk.END, show_content)
					self.textarea.focus()
				except:
					None
			# ----------------------------------------------------
			# Action Buttons
			self.btm_r_frame.pack(side='bottom', fill='both')
			# Delete Button
			self.del_btn.config(text='Delete Note', command=self.del_list_note)
			self.del_btn.pack(side='left', fill='both', ipady=10, expand=True)
			# Save Button
			self.save_btn.config(text='Update Note', command=self.update_list_note)
			self.save_btn.pack(side='right', fill='both', ipady=10, expand=True)
			# ----------------------------------------------------
		else:
			pass

	# _________________________________________________________________________
	def del_list_note(self):

		# Clear "Text-Area"
		self.textarea.delete(1.0, tk.END)

		# ----------------------------------------------------
		# Use selected item in listbox to determine file-name
		selected = self.listbox.curselection()
		if selected:
			# ----------------------------------------------------
			selected = int(selected[0])
			item = self.listbox.get(selected)

			if item == os.path.basename('Notes/' + str(item)):
				# Delete File
				try:
					os.remove('Notes/' + str(item))
				except:
					None

			# Clear the listbox item
			item = self.listbox.delete(selected)
			# ----------------------------------------------------
		else:
			pass
		# ----------------------------------------------------
		self.reset_app()

	# _________________________________________________________________________
	def update_list_note(self):

		# Grab content from "Text-Area"
		get_textarea = self.textarea.get(1.0, tk.END)

		# Use selected item in listbox to determine file-name
		selected = self.listbox.curselection()
		if selected:
			# ----------------------------------------------------
			selected = int(selected[0])
			item = self.listbox.get(selected)

			if item == os.path.basename('Notes/' + str(item)):
				# Write To File
				try:
					with open('Notes/' + str(item), 'w') as f_write:
						f_write.write(get_textarea + '\n')


				except:
					None
			# ----------------------------------------------------
		else:
			pass
		# ----------------------------------------------------
		self.reset_app()

	# _________________________________________________________________________
	def reset_app(self):

		self.left_col.destroy()
		self.right_col.destroy()
		App('')

# _________________________________________________________________________
def main():

	app = tk.Tk()
	App('')
	app.title('iNOTE')
	app.geometry('750x600')
	app.config(bg=white)
	app.mainloop()


# _________________________________________________________________________
if __name__ == '__main__':
	main()
