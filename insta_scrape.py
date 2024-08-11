import instaloader
import streamlit as st
import os

# Streamlit app
st.title("Instagram Profile Scraper")

# Input field for the target profile
target_profile = st.text_input("Enter the Instagram profile to scrape", "rajarani_coaching")

# Create a button to start scraping
if st.button("Scrape Profile"):
    # Initialize Instaloader
    bot = instaloader.Instaloader()

    try:
        # Load target profile without logging in
        profile = instaloader.Profile.from_username(bot.context, target_profile)

        # Display profile information
        st.write(f"**Username:** {profile.username}")
        st.write(f"**User ID:** {profile.userid}")
        st.write(f"**Number of Posts:** {profile.mediacount}")
        st.write(f"**Followers:** {profile.followers}")
        st.write(f"**Following:** {profile.followees}")
        st.write(f"**Bio:** {profile.biography}")
        st.write(f"**External URL:** {profile.external_url}")

        # Optionally download posts
        download_posts = st.checkbox("Download the latest 5 posts?")

        if download_posts:
            with st.spinner("Downloading posts..."):
                posts = profile.get_posts()

                # Create a directory to save the posts
                save_dir = f"{profile.username}_posts"
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)

                for index, post in enumerate(posts, 1):
                    bot.download_post(post, target=save_dir)
                    if index >= 5:  # Limit to the first 5 posts for demo purposes
                        break

            st.success("Posts downloaded successfully!")

        # Display followers and following lists
        show_followers = st.checkbox("Show Followers")
        show_following = st.checkbox("Show Following")

        if show_followers:
            st.write("**Followers:**")
            followers = [follower.username for follower in profile.get_followers()]
            st.write(", ".join(followers))

        if show_following:
            st.write("**Following:**")
            following = [following.username for following in profile.get_following()]
            st.write(", ".join(following))

    except instaloader.exceptions.ProfileNotExistsException:
        st.error("The profile does not exist.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
