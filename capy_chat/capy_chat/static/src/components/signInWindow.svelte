<div class="window sign-on-window mt-5">
	<div class="title-bar">
		<div class="title-bar-text">Sign On</div>
		<div class="title-bar-controls">
			<button aria-label="Minimize"></button>
			<button aria-label="Restore"></button>
			<button aria-label="Close"></button>
		</div>
	</div>
	<div class="window-body">
		<div class="grid grid-cols-1 divide-y divide-gray-400">
			<div class="sign-on-logo mb-2 flex items-end justify-center bg-cover">
				<p class="text-xl font-bold text-white">Capy Chat</p>
			</div>
			<div class="pt-1">
				<form>
					<div class="grid grid-cols-2 gap-x-6 gap-y-8 sm:grid-cols-6">
						<div class="sm:col-span-7">
							<!--Screen name-->
							<label for="username" class="block text-sm font-bold italic text-gray-900"
								>ScreenName</label
							>
							<div class="mt-1">
								<div
									class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
								>
									<input
										type="text"
										name="username"
										id="username"
										autocomplete="username"
										class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
										placeholder=""
									/>
								</div>
								<div>
									<a href="/register" class="text-blue-800 underline">Get a Screen Name</a>
								</div>
							</div>

							<!--Password-->
							<label for="password" class="block font-bold">Password</label>
							<div class="mt-1">
								<div
									class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md"
								>
									<input
										type="password"
										name="password"
										id="password"
										class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6"
									/>
								</div>
								<div>
									<a href="/forgot-password" class="text-blue-800 underline">Forgot Password?</a>
								</div>
							</div>

							<!--Sign on options-->
							<div class="mt-1">
								<div class="grid grid-cols-2 gap-4">
									<div>
										<input type="checkbox" id="save-password" name="save-password" />
										<label for="save-password">Save password</label>
									</div>
									<div class="justify-self-end">
										<label>
											<input type="checkbox" id="auto-login" name="auto-login" />
											<label for="auto-login">Auto-login</label>
										</label>
									</div>
								</div>
							</div>

							<!--Buttons-->
							<div class="mt-3">
								<div class="grid grid-cols-3 gap-4">
									<div>
										<button>?</button>
									</div>
									<div>
										<button>Setup</button>
									</div>
									<div>
										<button>Sign On</button>
									</div>
								</div>
							</div>

							<!--Version-->
							<div class="mt-3">
								<div class="grid grid-cols-1 gap-4">
									<div class="justify-self-center">Version 0.0.0.1</div>
								</div>
							</div>
						</div>
					</div>
				</form>
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	.sign-on-window {
		.title-bar {
			height: auto;
		}
	}
	.sign-on-logo {
		height: 250px;
		background-image: url('../images/capybara2.jpg');
		background-repeat: no-repeat;
	}
	.sign-on-button {
	}
</style>
