from webui.ui.ui import create_ui
from .args import args


def launch_webui():
    auth = (args.username, args.password) if args.username else None
    create_ui(args.theme).queue().launch(share=args.share, auth=auth)