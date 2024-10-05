<script lang="ts">
	import { onMount } from 'svelte';
	onMount(async () => {
		const clientID = 'capybaraenjoyer';
		const ws = new WebSocket(`ws://localhost:8000/ws/${clientID}`);
		ws.onmessage = function (event) {
			const messages = document.getElementById('messages');
			const message = document.createElement('li');
			const content = document.createTextNode(event.data);
			message.appendChild(content);
			//messages.appendChild(message);
		};
	});

	function connect() {
		const clientID = encodeURI('');
		const ws = new WebSocket(`ws://localhost:8000/ws/${clientID}`);
	}
</script>

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
				<form method="POST">
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
										value="capybaraenjoyer"
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
										value="capybaraenjoyer"
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
										<input type="checkbox" id="save-password" name="save-password" checked />
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
										<button title="Help" class="p-2">
											<svg
												xmlns="http://www.w3.org/2000/svg"
												width="24"
												height="24"
												fill="currentColor"
												class="bi bi-question-square-fill inline justify-self-center"
												viewBox="0 0 16 16"
											>
												<path
													d="M2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zm3.496 6.033a.237.237 0 0 1-.24-.247C5.35 4.091 6.737 3.5 8.005 3.5c1.396 0 2.672.73 2.672 2.24 0 1.08-.635 1.594-1.244 2.057-.737.559-1.01.768-1.01 1.486v.105a.25.25 0 0 1-.25.25h-.81a.25.25 0 0 1-.25-.246l-.004-.217c-.038-.927.495-1.498 1.168-1.987.59-.444.965-.736.965-1.371 0-.825-.628-1.168-1.314-1.168-.803 0-1.253.478-1.342 1.134-.018.137-.128.25-.266.25h-.825zm2.325 6.443c-.584 0-1.009-.394-1.009-.927 0-.552.425-.94 1.01-.94.609 0 1.028.388 1.028.94 0 .533-.42.927-1.029.927"
												/>
											</svg>
										</button>
									</div>
									<div>
										<button title="Setup" class="p-2">
											<svg
												xmlns="http://www.w3.org/2000/svg"
												width="24"
												height="24"
												fill="currentColor"
												class="bi bi-wrench inline justify-self-center"
												viewBox="0 0 16 16"
											>
												<path
													d="M.102 2.223A3.004 3.004 0 0 0 3.78 5.897l6.341 6.252A3.003 3.003 0 0 0 13 16a3 3 0 1 0-.851-5.878L5.897 3.781A3.004 3.004 0 0 0 2.223.1l2.141 2.142L4 4l-1.757.364zm13.37 9.019.528.026.287.445.445.287.026.529L15 13l-.242.471-.026.529-.445.287-.287.445-.529.026L13 15l-.471-.242-.529-.026-.287-.445-.445-.287-.026-.529L11 13l.242-.471.026-.529.445-.287.287-.445.529-.026L13 11z"
												/>
											</svg>
										</button>
									</div>
									<div>
										<button title="Sign On" class="p-2">
											<svg
												xmlns="http://www.w3.org/2000/svg"
												width="24"
												height="24"
												fill="currentColor"
												class="bi bi-box-arrow-in-right inline justify-self-center"
												viewBox="0 0 16 16"
											>
												<path
													fill-rule="evenodd"
													d="M6 3.5a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v9a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-2a.5.5 0 0 0-1 0v2A1.5 1.5 0 0 0 6.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 14.5 2h-8A1.5 1.5 0 0 0 5 3.5v2a.5.5 0 0 0 1 0z"
												/>
												<path
													fill-rule="evenodd"
													d="M11.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5H1.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708z"
												/>
											</svg>
										</button>
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
</style>
