INSERT INTO public.account_users(
	username, password, role, is_active, is_admin)
	VALUES ('admin', '$2b$12$pZjgBP1rWhFUtGHnsZYsleLo.azITU1ojxGgDqBkGXpayDwrl7jCC', 'common', true, true) ON CONFLICT DO NOTHING;