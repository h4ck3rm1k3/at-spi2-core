/*
 * AT-SPI - Assistive Technology Service Provider Interface
 * (Gnome Accessibility Project; http://developer.gnome.org/projects/gap)
 *
 * Copyright 2001, 2002 Sun Microsystems Inc.,
 * Copyright 2001, 2002 Ximian, Inc.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Library General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Library General Public License for more details.
 *
 * You should have received a copy of the GNU Library General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
 */

#ifndef ADAPTORS_H
#define ADAPTORS_H

#include <atk/atk.h>
#include <droute/droute.h>

Accessibility_Role spi_accessible_role_from_atk_role (AtkRole role);

void spi_initialize_accessible      (DRoutePath *path);
void spi_initialize_action          (DRoutePath *path);
void spi_initialize_application     (DRoutePath *path);
void spi_initialize_collection      (DRoutePath *path);
void spi_initialize_component       (DRoutePath *path);
void spi_initialize_document        (DRoutePath *path);
void spi_initialize_editabletext    (DRoutePath *path);
void spi_initialize_hyperlink       (DRoutePath *path);
void spi_initialize_hypertext       (DRoutePath *path);
void spi_initialize_image           (DRoutePath *path);
void spi_initialize_selection       (DRoutePath *path);
void spi_initialize_table           (DRoutePath *path);
void spi_initialize_text            (DRoutePath *path);
void spi_initialize_value           (DRoutePath *path);
void spi_initialize_tree            (DRoutePath *path);

#endif /* ADAPTORS_H */
